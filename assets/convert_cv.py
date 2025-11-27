#!/usr/bin/env python3
"""
CV Conversion Script
Converts CV from Markdown to HTML and PDF using pandoc with preset styling
Author: Anthony Onde Morada, MD

Usage: python3 convert_cv.py
"""

import subprocess
import sys
from pathlib import Path
import platform

def check_pandoc():
    """Check if pandoc is installed"""
    try:
        result = subprocess.run(['pandoc', '--version'], 
                              capture_output=True, check=True, text=True)
        version = result.stdout.split('\n')[0]
        print(f"✅ {version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        system = platform.system()
        print("❌ Error: pandoc is not installed")
        print("\n📦 Install pandoc:")
        if system == "Darwin":  # macOS
            print("  brew install pandoc")
        elif system == "Linux":
            print("  sudo apt install pandoc")
        elif system == "Windows":
            print("  winget install pandoc")
        print("  More info: https://pandoc.org/installing.html")
        return False

def check_latex():
    """Check if LaTeX is available for PDF generation"""
    latex_engines = ['xelatex', 'pdflatex', 'lualatex']
    
    print("Checking LaTeX engines...")
    for engine in latex_engines:
        try:
            result = subprocess.run([engine, '--version'], 
                          capture_output=True, check=True, text=True)
            print(f"✅ {engine} found")
            return engine
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"❌ {engine} not found")
            continue
    
    system = platform.system()
    print("⚠️  No LaTeX engine found (PDF generation disabled)")
    print("\nInstall LaTeX for PDF support:")
    if system == "Darwin":
        print("  brew install --cask mactex")
        print("  brew install --cask basictex  # smaller option")
    elif system == "Linux":
        print("  sudo apt install texlive-xetex texlive-fonts-recommended")
        print("  sudo dnf install texlive-xetex  # Fedora")
    elif system == "Windows":
        print("  Download MiKTeX: https://miktex.org/download")
        print("  Or TeX Live: https://tug.org/texlive/")
    return None

def find_cv_file():
    """Auto-detect CV markdown file"""
    possible_files = [
        "cv/anthony-onde-morada-cv.md",
        "anthony-onde-morada-cv.md", 
        "cv.md",
        "resume.md"
    ]
    
    for file_path in possible_files:
        if Path(file_path).exists():
            return Path(file_path)
    return None

def convert_to_html(input_file, output_file, css_file):
    """Convert markdown to styled HTML"""
    cmd = [
        'pandoc', str(input_file),
        '-f', 'markdown',
        '-t', 'html5',
        '--standalone',
        '--metadata', 'title=Curriculum Vitae',
        '-o', str(output_file)
    ]
    
    # Add CSS if it exists
    if css_file and css_file.exists():
        cmd.extend(['--css', str(css_file)])
        print(f"📎 Using stylesheet: {css_file}")
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ HTML: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ HTML generation failed")
        return False

def convert_to_pdf(input_file, output_file, latex_engine, css_file):
    """Convert markdown to PDF with preset formatting"""
    cmd = [
        'pandoc', str(input_file),
        '-f', 'markdown',
        '-o', str(output_file),
        f'--pdf-engine={latex_engine}'
    ]
    if css_file and css_file.exists():
        cmd.extend(['--css', str(css_file)])
       
    try:
        print("Running pandoc PDF conversion...")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ PDF: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ PDF generation failed")
        print(f"Command: {' '.join(cmd)}")
        print(f"Error details:")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        print(f"Return code: {e.returncode}")
        
        print(f"\nTroubleshooting:")
        print(f"1. Check if LaTeX packages are missing")
        print(f"2. Try simpler PDF generation")
        print(f"3. Use HTML to PDF: open HTML in browser, print to PDF")
        return False

def main():
    print("🔄 CV Conversion Script")
    print("=" * 40)
    
    # Check dependencies
    print("🔍 Checking requirements...")
    if not check_pandoc():
        sys.exit(1)
    
    latex_engine = check_latex()
    
    # Find input file
    input_file = find_cv_file()
    if not input_file:
        print("❌ CV markdown file not found")
        print("Expected locations:")
        print("  • cv/anthony-onde-morada-cv.md")
        print("  • anthony-onde-morada-cv.md")
        print("  • cv.md")
        print("  • resume.md")
        sys.exit(1)
    
    print(f"📄 Found CV: {input_file}")
    
    # Setup output
    output_dir = Path("cv")
    output_dir.mkdir(exist_ok=True)
    
    base_name = input_file.stem
    html_output = output_dir / f"{base_name}.html"
    pdf_output = output_dir / f"{base_name}.pdf"
    
    # Find CSS file
    css_file = Path("cv-style.css")
    if not css_file.exists():
        css_file = Path("cv-style.css")
    if not css_file.exists():
        css_file = None
        print("💡 No CSS file found - using default styling")
    
    print(f"📁 Output: {output_dir}/")
    
    # Convert files
    print("🔄 Converting...")
    
    html_success = convert_to_html(input_file, html_output, css_file)
    
    pdf_success = False
    if latex_engine:
        pdf_success = convert_to_pdf(input_file, pdf_output, latex_engine, css_file)
    else:
        print("⏭️  Skipping PDF (no LaTeX)")
    
    # Results
    print("=" * 40)
    if html_success or pdf_success:
        print("🎉 Conversion complete!")
        
        if html_success:
            print(f"🌐 HTML: {html_output}")
            print(f"   → Open in browser to preview")
        
        if pdf_success:
            print(f"📄 PDF: {pdf_output}")
            print(f"   → Ready for applications")
        else:
            print("📄 PDF: Failed - see error details above")
        
        print("\n📋 Next steps:")
        print("1. Review generated files")
        print("2. Customize cv-style.css if needed")
        print("3. Commit and push to update online CV")
        
    else:
        print("❌ Conversion failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
CV Conversion Script
Converts CV from Markdown to Word and PDF using pandoc
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
    """Find cv.md file"""
    cv_file = Path("cv.md")
    if cv_file.exists():
        return cv_file
    return None

def convert_to_docx(input_file, output_file, reference_doc=None):
    """Convert markdown to Word document with optional styling"""
    cmd = [
        'pandoc', str(input_file),
        '-f', 'markdown',
        '-t', 'docx',
        '-o', str(output_file)
    ]

    # Add reference document if provided
    if reference_doc and reference_doc.exists():
        cmd.extend(['--reference-doc', str(reference_doc)])
        print(f"📎 Using reference document: {reference_doc}")

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ Word: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Word generation failed")
        return False

def convert_to_pdf(input_file, output_file, latex_engine, css_file=None):
    """Convert markdown to PDF with optional styling"""
    cmd = [
        'pandoc', str(input_file),
        '-f', 'markdown',
        '-o', str(output_file),
        f'--pdf-engine={latex_engine}'
    ]

    # Add CSS if provided
    if css_file and css_file.exists():
        cmd.extend(['--css', str(css_file)])
        print(f"📎 Using stylesheet: {css_file}")

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
        print("❌ cv.md not found")
        sys.exit(1)

    print(f"📄 Found CV: {input_file}")

    # Setup output
    output_dir = Path("cv-downloads")
    output_dir.mkdir(exist_ok=True)

    docx_output = output_dir / "cv.docx"
    pdf_output = output_dir / "cv.pdf"

    # Check for optional styling files
    reference_doc = Path("assets/cv-reference.docx")
    css_file = Path("assets/style.css")

    if not reference_doc.exists():
        reference_doc = None
        print("💡 No reference document found - using default Word styling")
        print("   To customize Word: create assets/cv-reference.docx")

    if not css_file.exists():
        css_file = None
        print("💡 No CSS file found - using default PDF styling")
        print("   To customize PDF: assets/style.css already exists")
    else:
        print(f"📎 Found stylesheet: {css_file}")

    print(f"📁 Output: {output_dir}/")

    # Convert files
    print("🔄 Converting...")

    docx_success = convert_to_docx(input_file, docx_output, reference_doc)

    pdf_success = False
    if latex_engine:
        pdf_success = convert_to_pdf(input_file, pdf_output, latex_engine, css_file)
    else:
        print("⏭️  Skipping PDF (no LaTeX)")

    # Results
    print("=" * 40)
    if docx_success or pdf_success:
        print("🎉 Conversion complete!")

        if docx_success:
            print(f"📄 Word: {docx_output}")

        if pdf_success:
            print(f"📄 PDF: {pdf_output}")
        else:
            print("📄 PDF: Failed - see error details above")

    else:
        print("❌ Conversion failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
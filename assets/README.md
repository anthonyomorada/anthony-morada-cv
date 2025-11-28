# CV Conversion Assets

This directory contains the conversion script and optional styling files for generating your CV.

## Files

- `convert_cv.py` - Python script that converts `cv.md` to Word and PDF formats
- `style.css` - CSS stylesheet for web/HTML styling (already in use)
- `cv-reference.docx` - (Optional) Reference document for Word styling

## Usage

### Basic Conversion

Run the script from the project root:

```bash
python3 assets/convert_cv.py
```

This will:
- Read `cv.md` from the project root
- Generate `cv-downloads/cv.docx` (Word format)
- Generate `cv-downloads/cv.pdf` (PDF format)

### Customizing Styling

#### Word Document Styling

By default, the script uses pandoc's default Word styling. To customize:

1. **Generate a reference document:**
   ```bash
   pandoc --print-default-data-file reference.docx > assets/cv-reference.docx
   ```

2. **Customize the reference document:**
   - Open `assets/cv-reference.docx` in Microsoft Word
   - Modify the styles (fonts, colors, spacing, etc.)
   - Save the document

3. **Run the conversion again:**
   ```bash
   python3 assets/convert_cv.py
   ```

The script will automatically detect and use `assets/cv-reference.docx`.

#### PDF Styling

The script uses `assets/style.css` for PDF styling if it exists:

1. **Edit the CSS file:**
   - Modify `assets/style.css` to customize fonts, colors, spacing, etc.
   - The CSS includes sections for base styles, headings, links, lists, and print styles

2. **Run the conversion:**
   ```bash
   python3 assets/convert_cv.py
   ```

The script will automatically detect and apply `assets/style.css` to the PDF output.

### How It Works

- **Word (.docx)**: Uses `--reference-doc` if `assets/cv-reference.docx` exists, otherwise uses default pandoc styling
- **PDF (.pdf)**: Uses `--css` if `assets/style.css` exists, combined with LaTeX engine (xelatex, pdflatex, or lualatex)
- **Reproducibility**: By default, uses standard pandoc styling for consistent output across environments
- **Customization**: Add styling files to customize output while maintaining reproducibility for others

## Requirements

- Python 3
- pandoc (install via `brew install pandoc`)
- LaTeX engine for PDF (install via `brew install basictex` - optional but recommended)

## Tips

- Keep `cv-reference.docx` and `style.css` in version control for consistent custom styling
- The reference document affects Word output only
- The CSS file affects PDF output only
- Test your styling files after making changes
- Both files are optional - script works with default styling if not present

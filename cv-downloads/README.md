# CV Download Formats

This folder contains downloadable versions of Dr. Morada's curriculum vitae in multiple formats.

## Available Formats

- **PDF** - `cv.pdf`
- **Word** - `cv.docx`

## Generating CV Files

To generate PDF and Word versions from the markdown CV:
```bash
python3 assets/convert_cv.py
```

### Customizing Styling

**Default behavior**: Uses standard pandoc styling (reproducible across environments)

**To customize Word styling**:
1. Create a reference document: `assets/cv-reference.docx`
2. Modify styles in Word
3. Run the conversion script again

**To customize PDF styling**:
1. Edit the CSS file: `assets/style.css`
2. Modify fonts, colors, spacing, etc.
3. Run the conversion script again

See `/assets/README.md` for detailed instructions on customization.
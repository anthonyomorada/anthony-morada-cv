# Anthony Onde Morada, MD - CV Portfolio Website

[![Website](https://img.shields.io/badge/Website-Live-success?style=flat-square)](https://anthonyomorada.github.io/anthony-morada-cv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**Live Site:** [anthonyomorada.github.io/anthony-morada-cv](https://anthonyomorada.github.io/anthony-morada-cv/)

A professional portfolio website and CV repository for General Surgery residency and transplant surgery fellowship applications. Built with GitHub Pages and Jekyll for free, automated hosting.

---

## 🎯 Want to Create Your Own CV Website?

**This repository serves as a working example.** For a ready-to-use template with step-by-step instructions, see:

👉 **[am-medical-cv-template](https://github.com/anthonyomorada/am-medical-cv-template)** - Blank template for medical professionals

The template includes:
- ✅ Pre-configured Jekyll setup
- ✅ 5-minute quickstart guide
- ✅ No coding required
- ✅ Easy customization instructions

---

## 📁 Repository Structure

```
anthony-morada-cv/
├── index.md                    # Landing page with quick stats and highlights
├── cv.md                       # Complete curriculum vitae
├── README.md                   # This file - repository documentation
├── _config.yml                 # Jekyll configuration
├── LICENSE                     # MIT License
├── _includes/                  # Custom Jekyll components
│   └── footer.html
├── assets/                     # Images, CSS, and scripts
│   ├── profile-photo.png
│   ├── style.css
│   └── convert_cv.py          # Python script for PDF/Word conversion
├── cv-downloads/              # Downloadable CV files
│   ├── README.md
│   ├── cv.pdf
│   └── cv.docx
├── publications/              # Research papers PDFs
│   └── 2022-sr-ileostomy-malig.pdf
└── presentations/             # Conference posters and slides
    └── 2021-sages-poster.pdf
```

---

## 🚀 Quick Start

### View the Website
Simply visit: [anthonyomorada.github.io/anthony-morada-cv](https://anthonyomorada.github.io/anthony-morada-cv/)

### Download CV Files
- **PDF:** [cv-downloads/cv.pdf](cv-downloads/cv.pdf)
- **Word:** [cv-downloads/cv.docx](cv-downloads/cv.docx)

---

## 🛠️ How It Works

### GitHub Pages Hosting
This repository uses **GitHub Pages** with the **Jekyll static site generator** to automatically convert Markdown files into a professional website.

**Key Features:**
- ✅ **Free hosting** via GitHub Pages
- ✅ **Automatic updates** - push changes and site updates in ~1 minute
- ✅ **Mobile responsive** design optimized for program directors
- ✅ **No coding required** - edit Markdown files directly on GitHub
- ✅ **Custom domain support** (optional)

### File Types Explained

**Markdown Files (.md)**
- `index.md` - Homepage with stats and quick navigation
- `cv.md` - Full CV content in Markdown format
- Both auto-convert to HTML via Jekyll

**Downloads Folder (cv-downloads/)**
- Contains PDF and Word versions of CV
- Generated using Pandoc (see conversion script below)
- Updated manually when CV content changes

**Publications/Presentations**
- PDF files of research papers and conference materials
- Linked directly from CV for easy access

---

## ✏️ How to Update Your CV

### Method 1: Edit Directly on GitHub (Easiest)
1. Navigate to `cv.md` in the repository
2. Click the **pencil icon** (Edit this file)
3. Make changes in Markdown format
4. Scroll down and click **Commit changes**
5. Website updates automatically in ~1 minute

### Method 2: Local Editing
1. Clone the repository: `git clone https://github.com/anthonyomorada/anthony-morada-cv.git`
2. Edit `cv.md` and `index.md` in your text editor
3. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update CV content"
   git push origin main
   ```
4. GitHub Pages rebuilds automatically

---

## 📄 Converting CV to PDF/Word

This repository includes a Python script (`assets/convert_cv.py`) to convert the Markdown CV to PDF and Word formats using Pandoc.

### Prerequisites
```bash
# Install Pandoc
brew install pandoc          # macOS
sudo apt install pandoc      # Linux
# Windows: download from https://pandoc.org/installing.html

# Install LaTeX (for PDF generation)
brew install --cask mactex   # macOS
sudo apt install texlive-xetex  # Linux
```

### Run Conversion Script
```bash
python assets/convert_cv.py
```

This generates:
- `cv-downloads/cv.pdf` - Print-ready PDF
- `cv-downloads/cv.docx` - Editable Word document

### Manual Conversion (Alternative)
```bash
# Convert to PDF
pandoc cv.md -o cv-downloads/cv.pdf \
  --variable geometry:margin=0.75in \
  --variable fontsize=11pt

# Convert to Word
pandoc cv.md -o cv-downloads/cv.docx
```

---

## 🎨 Customization

### Styling
- Main stylesheet: `assets/style.css`
- Additional inline CSS in `index.md` between `<style>` tags
- Modify colors by changing CSS variables
- Main theme color: `--primary-color: #2c5aa0;`

### Profile Photo
- Replace `assets/profile-photo.png` with your own photo
- Recommended size: 400x400px minimum
- Format: PNG or JPG

### Contact Information
Update contact details in both:
- `index.md` - Contact section
- `cv.md` - Contact Information section

### Jekyll Configuration
- Edit `_config.yml` to customize site metadata
- Customize footer in `_includes/footer.html`

---

## 📂 Adding Publications and Presentations

### To Add a New Publication PDF:
1. Add PDF file to `publications/` folder
2. Update `cv.md` with link:
   ```markdown
   [[PDF](./publications/your-paper.pdf)]
   ```
3. Commit and push changes

### To Add a New Presentation:
1. Add PDF file to `presentations/` folder
2. Update `cv.md` with link:
   ```markdown
   [🖼️ PDF](./presentations/your-poster.pdf)
   ```
3. Commit and push changes

---

## 🔗 Using as a Template

**For the easiest setup experience, use the dedicated template repository:**

👉 **[am-medical-cv-template](https://github.com/anthonyomorada/am-medical-cv-template)**

### Alternative: Fork This Repository Directly
1. Click **Fork** button (top right)
2. Rename to `[your-username].github.io` or `[your-name]-cv`
3. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Select "Deploy from a branch"
   - Choose "main" branch
4. Edit `cv.md` and `index.md` with your information
5. Replace `assets/profile-photo.png` with your photo
6. Update `_config.yml` with your details
7. Replace publications/presentations PDFs with your own

---

## 📊 Built With

- **[GitHub Pages](https://pages.github.com/)** - Free static site hosting
- **[Jekyll](https://jekyllrb.com/)** - Static site generator (Minima theme)
- **[Markdown](https://www.markdownguide.org/)** - Simple content formatting
- **[Pandoc](https://pandoc.org/)** - Document conversion (Markdown → PDF/Word)

---

## 📬 Contact

**Anthony Onde Morada, MD**  
General Surgery Resident (PGY-4)  
Geisinger Northeast General Surgery Program

📧 anthony.omorada@gmail.com | amorada1@geisinger.edu  
📱 +1 (909) 239-3581

**Professional Profiles:**
- 🔬 [ORCID: 0000-0002-0428-6558](https://orcid.org/0000-0002-0428-6558)
- 💼 [LinkedIn](https://linkedin.com/in/anthonyomorada)
- 💻 [GitHub](https://github.com/anthonyomorada)

---

## 📄 License

This repository structure and template code is available under the [MIT License](LICENSE). Feel free to fork and adapt for your own professional CV website.

**Note:** CV content, publications, and personal materials remain copyright of Anthony Onde Morada, MD.

---

*Last updated: November 2025*

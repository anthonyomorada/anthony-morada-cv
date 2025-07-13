# Medical CV Template - GitHub Pages Portfolio

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green)](https://anthonyomorada.github.io/anthony-morada-cv/)
[![Template](https://img.shields.io/badge/Template-Ready-blue)](#quick-setup)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A GitHub Pages-hosted curriculum vitae with linked publications and presentations.

**Live Example:** [anthonyomorada.github.io/anthony-morada-cv](https://anthonyomorada.github.io/anthony-morada-cv/)

---

## Repository Structure

```
anthony-morada-cv/
├── index.md                        # Landing page
├── anthony-onde-morada-cv.md       # Complete CV
├── README.md                       # This file
├── _config.yml                     # GitHub Pages configuration
├── LICENSE                         # MIT license
├── .gitignore                      # Version control settings
├── cv/
│   ├── anthony-onde-morada-cv.pdf  # PDF version
│   └── styles.css                  # Custom styling
├── publications/
│   └── [PDF files]                 # Published papers
└── presentations/
    └── [PDF files]                 # Conference presentations
```

---

## Setup for Other Users

### Quick Start

1. Fork this repository
2. Replace content in `index.md` and `anthony-onde-morada-cv.md` with your information
3. Add your PDFs to `publications/` and `presentations/` folders
4. Enable GitHub Pages in repository Settings → Pages
5. Access your CV at `https://yourusername.github.io/repository-name/`

### File Naming Convention

- Publications: `YYYY-brief-title.pdf`
- Presentations: `YYYY-conference-title.pdf`

### Linking in CV

```markdown
Publication title. *Journal*. Year. [PDF](publications/filename.pdf)
Presentation title. *Conference*. Year. [Slides](presentations/filename.pdf)
```

---

## Technical Details

### Requirements

- GitHub account
- Basic Markdown knowledge
- Web browser for editing

### PDF Generation

- Use online Markdown to PDF converters
- Or Pandoc: `pandoc cv.pdf`

### Customization

- Edit `_config.yml` for site settings
- Modify `cv/styles.css` for appearance changes
- All editing can be done through GitHub's web interface

---

## Contact

**Anthony Onde Morada, MD**  
General Surgery Resident, Geisinger Northeast  
📧 [anthony.omorada@gmail.com](mailto:anthony.omorada@gmail.com)  
🔬 [ORCID: 0000-0002-0428-6558](https://orcid.org/0000-0002-0428-6558)

---

_MIT License - Free to use and modify_
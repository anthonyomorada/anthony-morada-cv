---
layout: default
---

<style>
:root {
  --primary-color: #2c5aa0;
  --primary-dark: #1a3a5c;
  --light-bg: #f8f9fa;
  --text-dark: #1a3a5c;
  --link-color: var(--primary-color);
  --link-visited: var(--primary-dark);
}

body {
  font-size: 16px;
  line-height: 1.6;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  color: var(--text-dark);
}

a {
  color: var(--link-color);
  text-decoration: none;
}

a:visited {
  color: var(--link-visited);
}

a:hover {
  text-decoration: underline;
}

/* Tighter paragraph and heading spacing */
p {
  margin: 0.7em 0;
}

h2 {
  margin-top: 1.1em;
  margin-bottom: 0.7em;
  border-bottom: none;
  padding-bottom: 0;
}

h1 {
  border-bottom: none;
  padding-bottom: 0;
}

hr {
  margin: 1em 0;
}

.hero-tagline {
  font-size: 1.2em;
  color: var(--text-dark);
  margin-bottom: 14px;
}

.hero-details {
  max-width: 720px;
  margin: 0 auto 14px;
}

.stat-card p {
  margin: 10px 0 0 0;
  font-size: 0.95em;
  color: var(--text-dark);
}

.featured-item .meta {
  color: var(--text-dark);
  font-size: 0.9em;
  margin: 10px 0;
}

.contact-badges {
  display: flex;
  gap: 8px;
  justify-content: center;
  flex-wrap: wrap;
  margin: 0px 0px;
}

.hero-section {
  text-align: center;
  padding: 18px 0 10px;
  margin-bottom: 8px;
}

.hero-section h1 {
  font-size: 2.5em;
  margin-bottom: 10px;
  color: var(--text-dark);
}

/* Stats grid - tighter spacing */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 16px;
  margin: 20px 0;
}

.stat-card {
  text-align: center;
  padding: 16px;
  background: var(--light-bg);
  border-radius: 8px;
  border-left: 4px solid var(--primary-color);
}

.stat-card h3 {
  font-size: 2.5em;
  margin: 0;
  color: var(--primary-color);
}

.nav-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin: 18px 0;
}

.nav-card {
  display: block;
  padding: 10px 16px;
  background: var(--primary-color);
  color: white;
  text-align: center;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  font-size: 1.1em;
  min-height: 48px;
  transition: background 0.3s ease;
}

.nav-card:visited {
  color: white;
}

.nav-card:hover {
  background: var(--primary-dark);
  color: white;
}

.featured-section {
  margin: 30px 0;
}

.featured-item {
  margin: 20px 0;
  padding: 20px;
  border-left: 4px solid var(--primary-color);
  background: var(--light-bg);
}

.featured-item h3 {
  margin-top: 0;
  color: var(--primary-color);
}

.featured-item .description {
  margin: 15px 0;
  line-height: 1.6;
}

.awards-list {
  display: grid;
  gap: 15px;
  margin: 20px 0;
}

.award-item {
  padding: 15px 20px;
  background: var(--light-bg);
  border-radius: 6px;
  border-left: 4px solid var(--primary-color);
}

.award-item strong {
  color: var(--primary-color);
}

.publication-list li {
  margin-bottom: 12px;
}

.updates-list {
  display: grid;
  gap: 10px;
  margin: 18px 0;
  padding-left: 0;
  list-style: none;
}

.updates-list li {
  padding: 12px 16px;
  background: var(--light-bg);
  border-left: 4px solid var(--primary-color);
  border-radius: 6px;
}

/* Mobile responsive */
@media (max-width: 768px) {
  body {
    font-size: 15px;
  }
  
  .hero-section {
    padding: 16px 0 12px;
    margin-bottom: 12px;
  }
  
  .hero-section h1 {
    font-size: 1.8em;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    margin: 18px 0;
  }
  
  .nav-cards {
    grid-template-columns: 1fr;
    margin: 18px 0;
  }
  
  .featured-section {
    margin: 20px 0;
  }
}
</style>

<div class="hero-section">
  <img src="assets/profile-photo.png" alt="Anthony Onde Morada, MD - Professional headshot" style="max-width: 200px; border-radius: 50%; margin: 0 auto 20px; display: block;">
  <h1>Anthony Onde Morada, MD</h1>
  <p class="hero-tagline">General Surgery Resident (PGY-4) | Surgical Education and Outcomes Research</p>
  <p class="hero-details">Geisinger Northeast General Surgery Program, Scranton, PA<br>
  Research interests in surgical education, hepatobiliary and transplant surgery, systematic reviews, and clinical outcomes.</p>
  
  <div class="contact-badges">
    <a href="https://orcid.org/0000-0002-0428-6558" target="_blank" rel="noopener">
      <img src="https://img.shields.io/badge/ORCID-0000--0002--0428--6558-green?style=flat-square&logo=orcid" alt="ORCID">
    </a>
    <a href="https://linkedin.com/in/anthonyomorada" target="_blank" rel="noopener">
      <img src="https://img.shields.io/badge/LinkedIn-anthonyomorada-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn">
    </a>
   <a href="https://github.com/anthonyomorada" target="_blank" rel="noopener">
      <img src="https://img.shields.io/badge/GitHub-anthonyomorada-black?style=flat-square&logo=github" alt="GitHub">
    </a>
  </div>
</div>

---

## Curriculum Vitae Access

<div class="nav-cards">
  <a href="cv.html" class="nav-card">
    View Full CV
  </a>
  <a href="cv-downloads/aom-cv.pdf" class="nav-card" download>
    Download PDF
  </a>
  <a href="cv-downloads/aom-cv.docx" class="nav-card" download>
    Download Word
  </a>
</div>

<p style="text-align: center; color: var(--text-dark); font-size: 0.9em; margin-top: 10px;">
  <em>Last Updated: May 2026</em><br>
  <a href="cv.html">View Full CV</a> • <a href="cv-downloads/">Download CV Files</a>
</p>

---

## Recent Updates

<ul class="updates-list">
  <li><strong>May 2026:</strong> Added two 2026 peer-reviewed publications in <em>Journal of Gastrointestinal Oncology</em> and <em>Trauma Surgery & Acute Care Open</em>, with full-text and PDF links.</li>
  <li><strong>May 2026:</strong> Presented surgical education work at the 2026 Association for Surgical Education Annual Meeting in Atlanta; manuscript in preparation for <em>Global Surgical Education</em>.</li>
  <li><strong>May 2026:</strong> Updated peer-review activity, published abstracts, and supporting publication PDFs to keep this electronic CV current and verifiable.</li>
</ul>

---

## Contact

**Institutional Email:** [amorada1@geisinger.edu](mailto:amorada1@geisinger.edu)  
**Personal Email:** [anthony.omorada@gmail.com](mailto:anthony.omorada@gmail.com)  
**Phone:** +1 (909) 239-3581  
**ORCID:** [0000-0002-0428-6558](https://orcid.org/0000-0002-0428-6558) • **LinkedIn:** [anthonyomorada](https://linkedin.com/in/anthonyomorada) • **GitHub:** [anthonyomorada](https://github.com/anthonyomorada)

---

## Research Impact

<div class="stats-grid">
  <div class="stat-card">
    <h3>11</h3>
    <p>Peer-Reviewed<br>Publications</p>
  </div>
  <div class="stat-card">
    <h3>31+</h3>
    <p>Conference<br>Presentations</p>
  </div>
  <div class="stat-card">
    <h3>92K+</h3>
    <p>Patients in Genomic<br>Data Analysis</p>
  </div>
  <div class="stat-card">
    <h3>$200K+</h3>
    <p>Fundraised for<br>Cancer Research</p>
  </div>
</div>

---

## Research Focus

**Systematic Reviews • Clinical Outcomes • Transplant Surgery**

From computational genomics at Geisinger's DiscovEHR to clinical research at Cedars-Sinai's Liver Transplant program, my work bridges data science and surgical innovation. Currently applying systematic review methodology and outcomes research to advance evidence-based surgical practice.

**Key Areas:**

- Transplant surgery outcomes and quality improvement
- Systematic reviews and meta-analyses in surgery
- Genomic medicine applications (92,297 patient cohort analysis)
- COVID-19 predictive modeling and triage algorithms

---

## Selected Publications

<ol class="publication-list">
<li>
<strong>Morada AO</strong>, Chen CK, Akateh C, Marvin MR, Kotru A. Hepatocellular Carcinoma Metastasis to Salivary Glands: A Systematic Review of Diagnostic Challenges and Survival Outcomes. <em>J Gastrointest Oncol</em>. 2026. <a href="https://doi.org/10.21037/jgo-2026-1-0015">Full Text</a> | <a href="publications/2026-jgo-hcc-salivary-glands.pdf">PDF</a>
</li>
<li>
<strong>Morada AO</strong>, Kropp Lopez A, Droney A, Lopez R. Traumatic Page kidney: a systematic review and patient report of bilateral Gerota's fascia release. <em>Trauma Surgery & Acute Care Open</em>. 2026;11:e002041. <a href="https://doi.org/10.1136/tsaco-2025-002041">Full Text</a> | <a href="publications/2026-tsaco-page-kidney.pdf">PDF</a>
</li>
<li>
Bashiri A, <strong>Morada AO</strong>, Sultany M, Senapathi S, Silverman S, Casós S, Behm R. Trends of Trauma Admissions in a Rural Trauma Center During Coronavirus Disease 2019 Pandemic. <em>J Surg Res</em>. 2023;289:202-210. PMID: 37141703. <a href="https://doi.org/10.1016/j.jss.2023.02.040">Full Text</a> | <a href="publications/2023-jsr-trauma-admissions.pdf">PDF</a>
</li>
</ol>

**[View all publications in full CV](cv.html#publications)**

---

## Research Experience Highlights

### **Cedars-Sinai Medical Center Liver Transplant Program** (2015-2017)
**Clinical Research Data Specialist** • Department of Liver Transplant & Hepatobiliary Surgery

- Coordinated clinical trials for liver transplant recipients and living donor candidates under Dr. Nicholas Nissen
- Managed transplant outcomes biorepository with specimens from 500+ transplant patients
- IRB contact for liver transplant clinical trials evaluating immunosuppression protocols and rejection outcomes
- Statistical analyses for transplant surgery research publications using R/SQL programming
- Direct collaboration with transplant surgery faculty on post-transplant outcomes research

### **Geisinger DiscovEHR Project** (2017-2018)
**Genomic Data Analyst** • Weis Center for Research

- Analyzed whole exome sequences from **92,297 patients** in one of the largest healthcare genomic databases
- R/Python programming for rare disease variant identification in autosomal dominant conditions
- Focus on genetic diseases relevant to transplant medicine and familial conditions
- Awarded competitive grant funding from Summer Research Immersion Program

**[View Full Research Timeline in CV](cv.html#research-experience)**

---

## Selected Recognition

<div class="awards-list">
  <div class="award-item">
    <strong>1st Place Oral & Poster Presentations</strong><br>
    Stanley Conklin Research Day (2021)
  </div>
  <div class="award-item">
    <strong>Hacking Health Innovation Winner</strong><br>
    $5,000 for Healthcare Innovation Project "ABBY" (2019)
  </div>
  <div class="award-item">
    <strong>#1 Fundraising Team - Two Consecutive Years</strong><br>
    Pancreatic Cancer Action Network (2016-2017)
  </div>
  <div class="award-item">
    <strong>Summer Research Grant Recipient</strong><br>
    Geisinger Commonwealth School of Medicine (2018)
  </div>
</div>

---

## Professional Memberships

- **International Liver Transplantation Society (ILTS)**
- **American Society of Transplant Surgeons (ASTS)**
- American College of Surgeons
- American Medical Association
- Pennsylvania Medical Society

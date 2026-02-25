# SF Match Publications Automation Guide

## Overview
This guide explains how to use the structured CSV file (`sf_match_publications.csv`) to automate filling out your SF Match publication entries.

## CSV Structure

The CSV contains **44 total entries** organized by SF Match categories:

### Publication Counts by Category
- **Peer-Reviewed Article (Published)**: 7 entries
- **Peer-Reviewed Article (Not Published)**: 4 entries (in review/preparation)
- **Peer-Reviewed Online Article (Published)**: 1 entry (preprint)
- **Non-Peer-Reviewed Online Article (Published)**: 2 entries
- **Oral Presentation**: 9 entries
- **Poster Presentation**: 21 entries

### CSV Columns
| Column | Description | Example |
|--------|-------------|---------|
| `Category` | SF Match publication category | "Peer-Reviewed Article (Published)" |
| `Title` | Full title of publication | "A systematic review of..." |
| `Authors` | Full author list | "Morada AO, Smith J, et al." |
| `Journal` | Journal or venue name | "Surg Endosc" |
| `Year` | Publication year | "2022" |
| `Volume` | Journal volume | "36" |
| `Issue` | Journal issue | "3" |
| `Pages` | Page numbers | "1750-1760" |
| `DOI` | Digital Object Identifier | "10.1007/s00464-021-08847-7" |
| `PMID` | PubMed ID | "34997348" |
| `Status` | Publication status | "Published", "In Review", "Accepted" |
| `Presentation_Location` | Venue for presentations | "SAGES Meeting, Las Vegas, NV" |
| `Presentation_Date` | Date of presentation | "August 2021" |
| `Notes` | Additional information | "Preprint", "Submitted", etc. |

## Automation Approaches

### Option A: CSV Upload via Browser Automation
Use the CSV with tools like:
- Selenium/Playwright (Python)
- Puppeteer (JavaScript)
- Browser extensions (Tampermonkey)

### Option B: Manual Copy-Paste Workflow
Use the CSV as a reference to systematically fill each entry, reducing typing errors.

### Option C: API Integration (if available)
Check if SF Match provides an API for bulk uploads.

## Example Python Script Template

```python
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Read the CSV
df = pd.read_csv('sf_match_publications.csv')

# Initialize browser
driver = webdriver.Chrome()
driver.get('https://sfmatch.org')

# Login (you'll need to handle authentication)
# ... login code ...

# Navigate to publications section
driver.find_element(By.LINK_TEXT, 'Publications').click()

# Iterate through each publication
for idx, row in df.iterrows():
    # Click "Add Publication"
    driver.find_element(By.XPATH, '//button[contains(text(), "Add Publication")]').click()

    # Select category from dropdown
    category_dropdown = Select(driver.find_element(By.ID, 'publication-category'))
    category_dropdown.select_by_visible_text(row['Category'])

    # Fill in fields based on category
    if 'Article' in row['Category']:
        driver.find_element(By.ID, 'title').send_keys(row['Title'])
        driver.find_element(By.ID, 'authors').send_keys(row['Authors'])
        driver.find_element(By.ID, 'journal').send_keys(row['Journal'])
        driver.find_element(By.ID, 'year').send_keys(str(row['Year']))

        if pd.notna(row['Volume']):
            driver.find_element(By.ID, 'volume').send_keys(str(row['Volume']))
        if pd.notna(row['Issue']):
            driver.find_element(By.ID, 'issue').send_keys(str(row['Issue']))
        if pd.notna(row['Pages']):
            driver.find_element(By.ID, 'pages').send_keys(row['Pages'])
        if pd.notna(row['DOI']):
            driver.find_element(By.ID, 'doi').send_keys(row['DOI'])
        if pd.notna(row['PMID']):
            driver.find_element(By.ID, 'pmid').send_keys(str(row['PMID']))

    elif 'Presentation' in row['Category']:
        driver.find_element(By.ID, 'title').send_keys(row['Title'])
        driver.find_element(By.ID, 'authors').send_keys(row['Authors'])
        driver.find_element(By.ID, 'location').send_keys(row['Presentation_Location'])
        driver.find_element(By.ID, 'date').send_keys(row['Presentation_Date'])

    # Click save
    driver.find_element(By.XPATH, '//button[contains(text(), "Save")]').click()

    time.sleep(2)  # Wait for save to complete

    print(f"Added: {row['Title']}")

driver.quit()
print("All publications added successfully!")
```

## Important Notes

1. **Verify Element IDs**: The example script uses placeholder element IDs. You'll need to inspect the SF Match form to get the actual field IDs.

2. **Handle Authentication**: Implement proper login handling before running automation.

3. **Error Handling**: Add try-except blocks to handle missing fields or form validation errors.

4. **Rate Limiting**: Add delays between entries to avoid overwhelming the server.

5. **Test First**: Test with 1-2 entries before running the full automation.

6. **Captcha/2FA**: If SF Match uses CAPTCHA or 2FA, you may need manual intervention.

## Quick Statistics

- Total publications to enter: **44**
- First author publications: **20**
- Co-author publications: **24**
- Date range: 2013-2026

## Next Steps

1. Inspect the SF Match form HTML to identify exact field names/IDs
2. Modify the script template with correct selectors
3. Test with 2-3 entries
4. Run full automation or use CSV for systematic manual entry
5. Verify all entries after completion

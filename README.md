# VaxLivestock – Smart Livestock Vaccination Monitoring & Fraud Detection

A zero-infrastructure, client-side web app that parses vaccination Excel/CSV files,
detects anomalies (GPS mismatch, duplicate images, expired vaccines, etc.) and
visualises risk scores instantly.

## Repository layout
```
vaccine-2.0/
├─ .gitignore
├─ README.md
├─ docs/
│   ├─ VaxLivestock_General_Report.html
│   ├─ VaxLivestock_Final_Report.html
│   ├─ VaxLivestock.pdf
│   └─ idtl final report.docx
├─ web/
│   ├─ index.html
│   ├─ part_head.html
│   ├─ part_body.html
│   └─ assets/logo.png
├─ data/
│   ├─ livestock_data.csv
│   └─ test data *.csv
├─ scripts/
│   └─ *.py
└─ presentation/
    └─ VaxLivestock.pptx
```

## Quick Start
1. Open `web/index.html` in a browser.
2. Click **Manage Data → Upload** and select any CSV from `data/`.
3. Review the risk-badge results; click **Print → Save as PDF** for a clean report.

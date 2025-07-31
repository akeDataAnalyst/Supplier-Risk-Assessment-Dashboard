# Supplier Risk Assessment Dashboard

### Project Overview
This project demonstrates how to build a proactive risk assessment tool for supply chain management. It combines traditional performance metrics with an NLP-driven geopolitical risk score to provide a holistic view of supplier reliability. The final deliverable is an interactive dashboard built in Tableau Public.

![Dashboard Screenshot](screenshots/dashboard_screenshot.png)

### The Problem & Solution
- **Problem:** Supply chain disruptions from poor supplier performance and unexpected global events can cause significant financial and operational damage.
- **Solution:** This dashboard provides a data-driven solution, enabling supply chain managers to identify high-risk suppliers and make informed decisions to mitigate potential disruptions.

### Methodology
1. **Data Generation:** Used Python with `pandas` and `numpy` to generate a synthetic dataset of supplier performance metrics (on-time delivery, quality scores).
2. **Geopolitical Risk Scoring (NLP):** Used a Python script to simulate news sentiment analysis, deriving geopolitical risk scores for each supplier's country.
3. **Risk Algorithm:** Created a weighted scoring model to combine performance and geopolitical risks into a single `total_risk_score`.
4. **Interactive Dashboard:** Built a professional, interactive dashboard in Tableau Public to visualize the results, including a risk heatmap and supplier details.

### Tools & Technologies
- **Data Analysis & Scripting:** Python, Pandas, NumPy
- **Natural Language Processing:** TextBlob
- **Data Visualization:** Tableau Public

### Access the Live Dashboard
You can explore the full, interactive dashboard here:
[**Live Dashboard Link on Tableau Public**](your_tableau_public_url_here)

---
*Created by AKLILU ABERA*

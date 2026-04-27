# 📊 Business Sales Performance Analytics
### Data Science & Analytics Internship Task 1 — Future Interns 2026

---

## 👤 Author
**Khethani Mugeri**  
 

---

## 📌 Project Overview

This project presents a full end-to-end business sales analysis of the Superstore dataset, 
the kind of analysis that data analysts perform for real companies, startups, and agencies.

The goal is not just to create charts, but to answer real business questions such as:
- Which products generate the most revenue?
- How do sales change over time?
- Which categories or regions are most profitable?
- Where should the business focus to grow faster?

---

## 📁 Project Structure

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core analysis and visualisation |
| Pandas | Data loading, cleaning, and analysis |
| Matplotlib | Chart creation and dashboard layout |
| Seaborn | Visual styling |
| LaTeX (Overleaf) | Professional report writing |
| Anaconda / Spyder | Development environment |

---

## 📊 Dataset

**Superstore Sales Dataset**  
Source: [Kaggle — Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

| Feature | Detail |
|---------|--------|
| Rows | 9,994 |
| Unique Orders | 5,009 |
| Time Period | 2014 – 2017 |
| Columns | Order ID, Product, Category, Region, Sales, Profit, Discount, Quantity |

---

## 🔍 Analysis Performed

### ✅ Stage 1 — Data Loading
- Loaded CSV using Pandas
- Previewed structure, column names, and data types

### ✅ Stage 2 — Data Cleaning
- Converted Order Date to datetime format
- Extracted Year and Month features
- Removed duplicate rows
- Verified missing values

### ✅ Stage 3 — Business Analysis
- Total revenue, profit, orders, and profit margin
- Sales and profit breakdown by Category
- Sales breakdown by Region
- Top 10 products by revenue
- Yearly sales trend (2014–2017)
- Sub-category sales vs profit comparison

### ✅ Stage 4 — Dashboard & Visualisation
- 5-panel professional dashboard
- KPI cards (Total Sales, Profit, Orders, Margin)
- Bar charts, line chart, and horizontal bar chart
- Saved as high-resolution PDF

---

## 📈 Key Findings

| Area | Finding | Value |
|------|---------|-------|
| Total Revenue | Full period sales | $2,297,201 |
| Total Profit | Full period profit | $286,397 |
| Profit Margin | Overall margin | 12.5% |
| Top Category | Highest revenue | Technology — $836,154 |
| Most Profitable | Highest profit | Technology — $145,455 |
| Weakest Category | Lowest profit margin | Furniture — 2.5% |
| Best Region | Highest sales | West — $725,458 |
| Weakest Region | Lowest sales | South — $391,722 |
| Revenue Growth | 2014 to 2017 | +52% |
| Top Product | Highest revenue product | Canon imageCLASS 2200 Copier |

---

## 💡 Business Recommendations

1.  **Investigate Furniture Profitability** — Revenue is high but margins are critically low at 2.5%
2.  **Invest More in Technology** — Best combination of revenue and profit margin
3.  **Grow the South Region** — Significant untapped revenue potential
4.  **Leverage Growth Momentum** — 52% growth trend; scale operations now
5.  **Review Machines Sub-Category** — High sales but near-zero or negative profit

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/khethaniMugeri/FUTURE_DS_01.git
```

2. Install dependencies:
```bash
conda install pandas matplotlib seaborn
```

3. Place `Superstore.csv` in the project folder

4. Run the analysis:
```bash
Python Code Task_1.py
```

5. The dashboard will be saved as `Sales_Dashboard_2026.pdf` in the same folder

---

## 📜 License
This project was completed as part of the Future Interns Data Science Internship Programme 2026.

---

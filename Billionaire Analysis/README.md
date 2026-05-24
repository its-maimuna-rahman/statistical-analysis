# Economic Analysis: Education, Wealth & Brain Drain Study

A comprehensive C-based analysis tool that examines the relationships between education, economic development, billionaire wealth distribution, and international brain drain across countries and over time.

---

## Project Overview

This project analyzes economic and demographic data to understand:
- How education impacts average national income
- The effect of billionaire wealth on income inequality
- The correlation between billionaire density and brain drain
- Bangladesh's unique case: economic growth vs. student emigration

The analysis is structured in 4 parts, each revealing different aspects of economic development and human migration patterns.

---

## Project Purpose and Contributors

This project was made by a group of 5 people (group 5) for academic purposes.

```
*** Group-5 Members ***

|              Name             | Roll No. |
|-------------------------------|----------|
| Maimuna Rahman                |    16    |
| Jannatul Mahabuba Adhora      |    05    |
| MD. Sharafatul Islam Shihab   |    49    |
| Zinna Tun Nahar Medha         |    27    |
| Zarin Subah                   |    38    |
```

```
*** Academic Details ***

Batch       :   31st
Course      :   CSE130 (Programming with C/C++)
Major       :   Applied Statistics And Data Science
Institute   :   Institute of Statistical Research and Training (ISRT)
University  :   University of Dhaka
```

## Project Structure

```
Billionaire-Analysis/
│
├── Necessary Codes/      # C source code and headers
│   ├── c_main.c
│   ├── econ_func.c
│   ├── economics.h
│   ├── stat_func.c
│   └── statistics.h
│
├── CSV Files/            # Raw datasets
│   ├── world.csv
│   └── bangladesh.csv
│
├── Visualization/        # Output graphs (PNG)
│   ├── analysis1_education_vs_salary.png
│   ├── analysis2_billionaire_effect.png
│   ├── analysis2_boxplot.png
│   ├── analysis3_brain_drain.png
│   ├── analysis4_bangladesh.png
│   └── analysis4_scatter.png
│
├── Analysis Result/      # Detailed report
│   └── Analysis Result.md
│
└── README.md             # This file
```

## How to Compile and Run

### Compilation
```bash
gcc -o analysis "Necessary Codes/c_main.c" "Necessary Codes/econ_func.c" "Necessary Codes/stat_func.c" -lm
```
(The `-lm` flag links the math library for `sqrt()`, `pow()`, etc.)

### Execution
```bash
./analysis
```

The program will:
1. Load data from `CSV Files/`
2. Run all 4 analyses
3. Output comprehensive tables, statistics, and interpretations

---

## Data Files

### CSV Files/world.csv
Global dataset containing information on multiple countries:
| Column | Description |
|---|---|
| `avg_education` | Average years of formal education |
| `avg_salary` | Average annual salary (USD) |
| `income_with_billionaire` | Total national income including billionaires |
| `population_with_billionaire` | Total population |
| `income_without_billionaire` | Total income excluding billionaires |
| `population_without_billionaire` | Non-billionaire population |
| `billionaire_left` | Number of billionaires who emigrated |
| `billionaire_born` | Number of billionaires born/produced in the country |

### CSV Files/bangladesh.csv
Time-series data for Bangladesh (1975-2025):
| Column | Description |
|---|---|
| `year` | Calendar year |
| `gdp_per_capita` | GDP per capita (USD) |
| `population` | Total population |
| `students_out` | Number of students studying abroad |
---

## Research Questions

| # | Analysis | Research Questions |
|---|---|---|
| 1 | Per Capita Income Regression | Do educated countries earn more? How much does each year of education add to income? |
| 2 | Billionaire Effects Analysis | Is the reported "average income" realistic? How much do billionaires skew national income statistics? |
| 3 | Brain Drain vs Billionaire Density | Do successful countries retain their talent? Which countries are losing — or keeping — their best people? |
| 4 | Bangladesh Case Study | Does Bangladesh's economic development reduce brain drain? |

---

## Analysis Summary & Key Findings

| # | Analysis | Method | Key Finding |
|---|---|---|---|
| 1 | Education vs Income | Linear Regression | r = 0.6526 — moderate positive correlation |
| 2 | Billionaire Wealth Distortion | Univariate + IQR Outlier Detection | Only 1.75% inflation effect on national averages |
| 3 | Brain Drain vs Billionaire Density | Bivariate Correlation | r = −0.2050 — weak correlation |
| 4 | Bangladesh: Growth vs Brain Drain | Time-series Correlation | r = 0.1650 — growth and emigration are independent |
---

### Overall Conclusion
- **The Education Dividend:** Education moderately predicts national income (r = 0.6526) — each extra year of schooling adds ~$5,410 to average salary, but structural factors still play a major role.
- **The Billionaire Paradox:** We often perceive billionaires as the primary drivers or distorters of a nation's economic reality. Despite astronomical individual wealth, billionaires inflate the global average income by only 1.75% — far less distortion than public discourse suggests.
- **The Talent Retention Gap:** Producing billionaires doesn't mean keeping them (r = −0.2050). Small nations lose all their top talent; large developed economies retain most.
- **The Bangladesh Dilemma:** GDP grew 10×, yet student emigration grew 190× over 50 years (r = 0.1650). Economic growth alone does not reduce brain drain — As the country grew wealthier, student emigration grew even faster. Retaining talent requires more than GDP growth; it demands systemic improvements in opportunity and quality of life that can compete with what destination countries offer.

For complete results, figures, methodology, and discussion → see [`Analysis Result/Analysis Result.md`](Analysis%20Result/Analysis%20Result.md).
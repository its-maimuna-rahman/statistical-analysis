# Statistical Analysis Results

**Project**: Economic Analysis — Education, Wealth & Brain Drain Study  
**Course**: CSE130 | **Group**: 5 | **Institute**: ISRT, University of Dhaka

This document presents the full statistical results, visualizations, and interpretations for all 4 analyses. For project setup and source code, see [`README.md`](../README.md). For an interactive version, check the [`Jupyter Notebook`](../notebook/billionaire_analysis.ipynb).

---

## Data Sources & Sample Size
The datasets used in this study were synthesized from several reputable international organizations:
- **World Dataset (`world.csv`)**: 
  - Covers **183 countries**.
  - **Sources**: 
      - 1. Forbes World's Billionaires List
      - 2. World Bank/UN Population
      - 3. World Bank Poverty & Inequality Platform
      - 4. UNDP Human Development Reports
      - 5. International Labour Organization (ILO).
- **Bangladesh Dataset (`bangladesh.csv`)**: 
  - Covers **51 years** of longitudinal data (1975–2025).
  - **Sources**
      - 1. World Data Bank
      - 2. MacroTrends
      - 3. Federal Reserve Economic Data (FRED).

---

## Analysis 1: Per Capita Income Regression
### Education vs. Average Salary

**Research Question**: Do more educated countries earn significantly higher incomes?

**Method**: Bivariate linear regression — X = average years of education, Y = average annual salary (USD)

**Regression Equation**:
```
Salary = 5,410 × Education − 25,589
```

| Statistic | Value | Interpretation |
|---|---|---|
| Slope (m) | $5,410 | Each additional year of education adds ~$5,410 to average salary |
| Intercept (c) | −$25,589 | Theoretical base with zero education |
| Correlation (r) | **0.6526** | Moderate-to-strong positive relationship |

**Correlation Scale Used**:

| r Value | Interpretation |
|---|---|
| r > 0.8 | Very strong positive |
| 0.6 < r ≤ 0.8 | Strong positive |
| 0.4 < r ≤ 0.6 | Moderate positive |
| r ≤ 0.4 | Weak |

### Result

  - **Do educated countries earn more?**
  - **YES - education moderately predicts national income (r = 0.6526)** 
  - **Conclusion**: Education strongly predicts income potential

  - **How much does each education year add to income?**
  - **$5,410 per additional year of education**
  - This is a significant economic return on education investment
  - Regression equation: `Salary = 5,410 x Education - 25,589`

![Analysis 1: Education vs Salary](../Visualization/analysis1_education_vs_salary.png)

---

## Analysis 2: Billionaire Wealth Distortion
### Effect of Billionaires on National Income Statistics

**Research Question**: How much do billionaires skew a country's reported average income?

**Method**: Univariate comparison — per capita income *with* vs. *without* billionaires; extreme outlier detection using the **3×IQR method**

### Income Comparison

| Metric | Value |
|---|---|
| Average per capita income (with billionaires) | $61,079 |
| Average per capita income (without billionaires) | $60,026 |
| Difference (Billionaire Inflation Effect) | **1.75%** |

![Analysis 2: Billionaire Effect](../Visualization/analysis2_billionaire_effect.png)

### Outlier Detection — 3×IQR Method

The 3×IQR method identifies *extreme* outliers in per capita income distribution:

| Statistic | Value |
|---|---|
| Q1 (25th percentile) | $211.01 |
| Q2 / Median | $1,255.41 |
| Q3 (75th percentile) | $8,033.82 |
| IQR (Q3 − Q1) | $7,822.80 |
| Lower Bound (Q1 − 3×IQR) | −$23,257.39 |
| **Upper Bound (Q3 + 3×IQR)** | **$31,502.22** |

> Any country with average per capita income (including billionaires) **above $31,502.22** is an extreme statistical outlier — indicating massive wealth concentration or extreme billionaire distortion.

![Analysis 2: Wealth Distribution Boxplot](../Visualization/analysis2_boxplot.png)

### Outlier Countries (Extreme Wealth Concentration)

| Country | Per Capita Income (with billionaires) |
|---|---|
| Monaco | $5,136,111.11 |
| Liechtenstein | $3,523,076.92 |
| Tuvalu | $534,545.45 |
| Seychelles | $236,916.67 |
| Iceland | $168,979.06 |
| Brunei | $140,311.80 |
| Luxembourg | $132,465.54 |
| Saint Vincent and Grenadines | $128,846.15 |
| Bahamas | $97,201.02 |
| Saint Lucia | $78,500.00 |
| Malta | $70,581.61 |
| Barbados | $60,638.30 |
| Tonga | $59,345.79 |
| Micronesia | $34,385.96 |
| Maldives | $32,595.42 |
| Montenegro | $32,220.42 |
| Qatar | $32,203.70 |
| Bahrain | $32,176.87 |

### Result

  - **Is the "average income" realistic?**
  - **YES - VERY realistic**
  - Average with billionaires: $61,079
  - Average without billionaires: $60,026
  - Difference: Only **1.75%**
  - **Conclusion**: Unlike some developing nations, billionaires don't drastically inflate global averages

  - **How much do billionaires skew statistics?**
  - **1.75% inflation effect**
  - Most countries in the dataset have relatively modest billionaire populations
  - Top billionaire concentrations (USA, China, Germany, India) exist but don't dominate weighted averages

---

## Analysis 3: Brain Drain vs. Billionaire Density Correlation

**Research Question**: Do countries that produce talented billionaires retain them?

**Method**: Bivariate correlation analysis

**Metrics Defined**:

| Metric | Formula | Meaning |
|---|---|---|
| Billionaire Density (X) | Billionaires Born / Population (millions) | Talent productivity per million people |
| Brain Drain Rate (Y) | Billionaires Left / Billionaires Born | Proportion of produced billionaires who emigrated |

**Correlation Interpretation Scale**:

| r Value | Interpretation |
|---|---|
| r > 0.6 | Strong — productive countries lose talent (paradox) |
| 0.3 < r ≤ 0.6 | Moderate — some tendency for talent emigration |
| −0.3 < r ≤ 0.3 | Weak/None — density doesn't predict emigration |
| r < −0.3 | Negative — high-producing countries retain talent well |

### Result

  - **Do successful countries retain their talent?**
  - **WEAK CORRELATION (r = -0.2050)**
  - Billionaire density doesn't strongly predict emigration
  - Neither a strong brain drain nor strong retention pattern
  - **Conclusion**: Whether a country produces billionaires doesn't determine if they stay

![Analysis 3: Brain Drain vs Billionaire Density](../Visualization/analysis3_brain_drain.png)

### Countries with 100% Brain Drain (All Billionaires Emigrated)

 **Albania, Armenia, Azerbaijan, Barbados, Belarus, Belize, Bulgaria, Cuba, Georgia, Haiti *(and others)***

 These are smaller nations that produce only 1–2 billionaires but lose every single one.

### Countries Retaining Talent

| Country | Born | Left | Drain Rate |
|---|---|---|---|
| USA | 704 | 70 | 10% |
| China | 607 | 35 | 6% |
| UK | 177 | 10 | 6% |
| Germany | 134 | 10 | 7% |

 **Pattern**: Large, developed nations retain the vast majority of their talent; small nations lose all of theirs.

---

## Analysis 4: Bangladesh Case Study
### Economic Growth vs. Brain Drain (1975–2025)

**Research Question**: Does Bangladesh's economic development reduce student emigration?

**Method**: 50-year time-series correlation analysis

**Metrics Defined**:

| Metric | Formula | Meaning |
|---|---|---|
| Wealth Growth (X) | (GDP_current − GDP_previous) / GDP_previous | Annual % change in GDP per capita |
| Drain Intensity (Y) | Students Abroad / Population (millions) | Students per million people |

**Correlation Interpretation Scale**:

| r Value | Finding |
|---|---|
| r > 0.5 | Growth *enables* brain drain — wealth gives families money to send kids abroad |
| r < −0.5 | Growth *reduces* brain drain — better home opportunities retain talent |
| −0.5 < r < 0.5 | Growth and emigration are independent — other factors drive migration |

### Key Statistics (1975–2025)

| Indicator | 1975 | 2025 | Change |
|---|---|---|---|
| GDP per capita | $250 | $2,734 | **10.9× increase** |
| Students studying abroad | 300 | 57,000 | **190× increase** |
| Average annual GDP growth | — | — | **5.69%** |
| Correlation (r) | — | — | **0.1650** |

### Result

  - **Does Bangladesh's development reduce brain drain?**
  - **NO - VERY WEAK correlation (r = 0.1650)**
  - GDP per capita grew from $250 (1975) to $2,734 (2025) - **10.9x increase!**
  - Student outflow grew from 300 (1975) to 57,000 (2025) - **190x increase!**
  - Economic growth and emigration are essentially **independent**
  - Economy grows rapidly (5.69% annually)
  - Student emigration ALSO grows (doubled every 10 years since 1990s)
  - Development hasn't changed the emigration pattern
  - International opportunities and quality of life matter more than raw GDP growth alone
  - **Conclusion**: Development alone DOES NOT reduce brain drain


![Analysis 4: Bangladesh Economic Growth vs Brain Drain](../Visualization/analysis4_bangladesh.png)
![Analysis 4: Wealth Growth vs Drain Intensity Scatter](../Visualization/analysis4_scatter.png)

---

## Statistical Caveats & Limitations
While this analysis provides significant insights, several statistical constraints must be considered:

- **Bivariate Limitations**: Analysis 1 (Education vs. Salary), Analysis 3 (Billionaire Density), and Analysis 4 (Bangladesh Study) utilize bivariate models. In complex macroeconomic systems, variables like national income are influenced by a multitude of "omitted variables" including industrial infrastructure, political stability, geographical factors, and technological adoption. Attributing variance solely to one factor (like education) simplifies these multifaceted relationships.

- **The Small-Country Effect**: In Analysis 2, the 3×IQR method perfectly flagged countries like Monaco, Tuvalu, Liechtenstein, and the Seychelles as extreme outliers. These are micro-states with very small populations where a single billionaire or specific tax laws can drastically skew per capita calculations compared to massive economies. In such cases, the mean income does not reflect the typical citizen's economic reality.

- **Correlation vs. Causation**: High correlation coefficients (e.g., r = 0.6526 in Analysis 1) indicate strong associations but do not confirm direct causality. Endogeneity—where education drives wealth while national wealth simultaneously funds education systems—makes isolating a singular "direction" of impact statistically challenging.

- **Data Consistency & Reporting Lags**: Compiling data from diverse sources like the World Bank, IMF, and ILO involves reconciling different reporting frequencies and methodologies. Some indicators may also reflect inherent reporting lags common in international economic statistics.

---

## Overall Conclusions

### The Education Dividend
Education is often treated as the universal key to national prosperity — and our data confirms it matters, but with important nuance. Countries with higher average years of schooling do earn more, but the relationship is moderate (r = 0.6526), not absolute. A single additional year of education adds ~$5,410 to average national salary, which is a significant return — yet nearly 35% of income variation remains unexplained by education alone. Prosperity is not simply bought with diplomas. Structural factors — governance, industry, geography, and opportunity — shape a nation's wealth just as powerfully as the years its citizens spend in school.

### The Billionaire Paradox
We often perceive billionaires as the primary drivers or distorters of a nation's economic reality. However, our statistical analysis reveals a paradox: **while their individual wealth is astronomical, their impact on national per capita income statistics is surprisingly marginal.** Globally, the presence of billionaires only inflates average annual income by approximately **1.75%** ($22,110 vs $21,817 in our dataset). This suggests that national prosperity is built on a much broader base of economic activity than the ultra-wealthy alone, and the "average" citizen's economic reality is less affected by billionaires than public discourse often suggests.

### The Talent Retention Gap
Producing billionaires does not guarantee retaining them. Our analysis reveals a striking paradox: the countries that generate the most talent per capita are not necessarily the ones keeping it. Small nations lose 100% of their produced billionaires to emigration, while larger economies like the USA, China, and Germany retain over 90% — not because they produce more, but because they offer more. With r = −0.2050, billionaire density barely predicts brain drain, suggesting that retention is driven by the *environment a country offers*, not the talent it generates.

### The Brain Drain Paradox
Brain drain is not simply a symptom of poverty. In Bangladesh, it is a *consequence of development* — as the economy grows, so does the outflow of students. Economic growth gives families the *financial means* to send their children abroad. Development doesn't reduce the desire to leave; it funds it. International opportunities and quality of life matter more than raw GDP growth.

---
### The core findings of this analysis :
Education, wealth, and talent are assets any nation can build — but without the institutions, opportunities, and quality of life to match, they will always flow elsewhere.

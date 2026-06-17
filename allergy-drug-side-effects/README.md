# Side‑Effect Analysis: Food‑Allergy Medications Study

A comprehensive statistical analysis of side‑effect profiles in food‑allergy medications, examining patterns across different drugs, age groups, biological sexes, and countries of reporting. (Full analysis report : [`analysis_result/analysis_result.md`](analysis_result/analysis_result.md))

---

## Project Overview

This project analyzes real‑world pharmacovigilance data to understand:
- Drug‑specific side‑effect "fingerprints" for common allergy medications.
- How age (child, adult, elderly) influences the risk of specific adverse events.
- Gender‑based differences in side‑effect prevalence.
- Geographic variations in reported side effects across countries (USA, UK, Canada, France, Germany, Japan).

The analysis utilizes descriptive statistics, chi‑square tests, Fisher's exact tests, odds ratios, and logistic regression to produce actionable safety profiles.

---

## Project Structure

```
allergy-drug-side-effects/
│
├── analysis_result/      # Detailed report and source documents
│   ├── analysis_result.md
│   └── allergy_analysis_paper.pdf
│
├── dataset/              # Raw and processed datasets
│   └── allergy_dataset.csv
│
├── visualizations/        # Output graphs (PNG)
│   ├── 4.1.1_top_side_effects_per_drug.png
│   ├── 4.1.2_drug_side_effect_heatmap.png
│   ├── 4.2.1_age_stratified_patterns.png
│   ├── 4.3.1_gender_stratified_patterns.png
│   ├── 4.4.1_country_stratified_patterns.png
│   └── ... (and others)
│
├── outline/              # Project planning documents
│   └── allergy_med_outline.md
│
└── README.md             # This file
```

---

## Data Files

### dataset/allergy_dataset.csv
A structured pharmacovigilance‑style dataset containing 653 records. Each record represents a reported adverse event:
| Column | Description |
|---|---|
| `drug` | The medication name (e.g., Epinephrine, Albuterol, Diphenhydramine) |
| `age_group` | Categorical: Child (0‑12), Adult (13‑64), Elderly (65+) |
| `gender` | Biological sex (Male, Female) |
| `country` | Country of reporting |
| `[side_effect]` | 18 binary (0/1) flags for specific side effects (e.g., sedation, nausea, cardiovascular_problem) |

---

## Research Questions

| # | Analysis | Research Questions |
|---|---|---|
| 1 | Drug‑Specific Patterns | Which specific drugs are associated with which specific side effects overall? |
| 2 | Age‑Stratified Analysis | How do these patterns change by age group (child, adult, elderly)? |
| 3 | Gender‑Specific Patterns | Are there gender‑specific patterns (e.g., more sedation or cardiovascular events in one gender)? |
| 4 | Country‑Specific Patterns | Are there country‑specific patterns (e.g., higher sedation rates in one country vs another)? |
| 5 | High‑Risk Combinations | Are there high‑risk combinations (drug + age + gender + country) for certain side effects? |

---

## Analysis Summary & Key Findings

| # | Analysis | Method | Key Finding |
|---|---|---|---|
| 1 | Drug Comparison | Descriptive Frequencies | Albuterol & Hydrocortisone have the highest per‑patient burden. |
| 2 | Age Dependence | Chi‑square & Heatmaps | Children have highest cardiovascular (39.4%) and sedation (36.5%) rates. |
| 3 | Gender Differences | Fisher's Exact Test | Females show significantly higher cardiovascular and nausea rates. |
| 4 | Country Comparison | Odds Ratio Analysis | UK has significantly higher odds of sedation (OR=1.87) vs. USA. |
| 5 | Multivariate Risk | Logistic Regression | Drug choice is the primary determinant of sedation risk. |

---

## Overall Conclusion
- ### The Drug Factor:
 Medication choice is the strongest predictor of adverse events. Albuterol and Hydrocortisone emerged as high‑burden agents, while second‑generation antihistamines like Cetirizine showed significantly better safety profiles than first‑generation agents.
- ### The Pediatric Vulnerability:
 Children bear a disproportionate burden of serious side effects, particularly cardiovascular events (39.4%) and sedation. This underscores the critical need for pediatric‑specific dosing and monitoring.
- ### The Gender Gap:
 Biological sex plays a significant role in side‑effect manifestation, with females experiencing higher rates of cardiovascular and gastrointestinal symptoms, likely due to pharmacokinetic or hormonal differences.
- ### The Geographic Variance:
 Side‑effect reporting is not uniform globally. The UK exhibits significantly higher odds for several serious side effects (sedation, cardiovascular, adrenal suppression) compared to the USA, suggesting differences in clinical practice or reporting cultures.

--- 

For complete results, figures, methodology, and discussion → see [`analysis_result/analysis_result.md`](analysis_result/analysis_result.md).

# ML-model-for-cyanobacteria-growth

# Raman Spectroscopy Analysis: Glucose & Ethanol Prediction

This project focuses on predicting the concentration of **glucose** and **ethanol** in yeast cultures using **Raman spectroscopy** data. By accurately monitoring these metabolites, we can infer the biomass (yeast quantity) throughout the fermentation process.

---

## Context & Data Source

The dataset used in this project consists of **real-world experimental measurements** obtained from the **Chair of Biotechnology at CentraleSupélec**

Unlike synthetic datasets, these measurements reflect actual laboratory conditions. As a result, the spectral data contains significant **experimental noise**, presenting a realistic challenge for signal processing and regression modeling.

---

## Methodology

To handle the noisy nature of the data and predict concentrations effectively, we implemented and compared three distinct Machine Learning approaches:

1.  **Linear Regression (AUC-based):**
    * A physics-informed approach that calculates the **Area Under the Curve** of specific Raman peaks known to correlate with glucose and ethanol bonds. A simple linear regression is then applied to these areas.

2.  **Partial Least Squares (PLS):**
    * A statistical method particularly well-suited for spectroscopy, as it handles collinearity in the spectral data by projecting the predicted variables and the observable variables to a new space.

3.  **Support Vector Regression (SVR):**
    * Used to capture potential non-linear relationships between the spectral intensity and metabolite concentrations.

---

## Project Structure


# project strucure 

```bash
├── data/               # Raw and processed Raman spectra
├── notebooks/          # Jupyter notebooks for EDA and model comparison
├── src/                # Python scripts for preprocessing and modeling             
├── plots/              # Generated figures (Spectra, Regression lines)
└── README.md
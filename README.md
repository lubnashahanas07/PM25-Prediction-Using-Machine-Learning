# Evaluation of the Predictive Gain of Meteorological Variables in Machine Learning-Based PM2.5 Prediction: A Case Study of Anand Vihar, New Delhi 

## Project Overview

This project evaluates the performance of machine learning models in predicting PM₂.₅ concentrations using atmospheric composition variables from CAMS reanalysis data, with a particular focus on assessing whether the inclusion of meteorological variables improves predictive performance.Hourly PM₂.₅ observations from the Central Pollution Control Board (CPCB) were integrated with three hourly atmospheric composition and meteorological data from the Copernicus Atmosphere Monitoring Service (CAMS) for Anand Vihar, New Delhi, over the study period 2016–2025.

Initially, models were developed using atmospheric composition variables to predict PM₂.₅ concentrations. Meteorological variables were subsequently incorporated into the feature set, and the predictive performance of the models was compared to assess the contribution of meteorological information. Following this comparison, the combined atmospheric composition and meteorological variables were used for further model development, evaluation, and hyperparameter tuning.

The project also includes an interactive Streamlit application for PM₂.₅ prediction using the trained model.

## Objectives

- To develop machine learning models for predicting PM₂.₅ concentrations using atmospheric composition variables.
- To investigate the influence of incorporating meteorological variables alongside atmospheric composition variables on the     predictive performance of machine learning models.
- To identify an appropriate feature set and machine learning model for PM₂.₅ prediction through comparative model evaluation.
- Develop an interactive application for PM₂.₅ prediction.

## Study Area

**Anand Vihar, New Delhi, India**

Anand Vihar is an urban area known for elevated particulate matter concentrations and significant air pollution episodes. It was selected as the study location for investigating the relationship between atmospheric variables and ground-level PM₂.₅ concentrations.

## Data Sources

### 1. Ground-Level PM₂.₅ Observations

- **Source:** Central Pollution Control Board (CPCB), India
- **Variable:** PM₂.₅ concentration
- **Temporal resolution:** Hourly
- **Study period:** 2016–2025

### 2. Atmospheric Composition and Meteorological Data 

- **Source:** CAMS(Copernicus Atmosphere Monitoring Service) global reanalysis(EAC4)
- **Temporal resolution:** 3-hourly
- **Data:** 
    Atmospheric Composition Variables (12):- 
    
    Carbon monoxide (CO), dust aerosol mixing ratios across different size ranges (AERMR04, AERMR05, AERMR06), hydrophilic and hydrophobic black carbon and organic matter aerosols (AERMR09, AERMR07, AERMR10, AERMR08), nitrogen dioxide (NO₂), nitrogen monoxide (NO), ozone (O₃), and sulphur dioxide (SO₂).

    Meteorological Variables (6):-
    
    Specific humidity (Q), surface temperature (T), zonal and meridional wind components at 10 m (U10, V10), 2 m dew point temperature (D2M), and 2 m temperature (T2M).

- **Study period:** 2016–2025

## Methodology

The project followed a systematic workflow involving data acquisition, integration, preprocessing, exploratory data analysis, feature assessment, model development, and evaluation.

### 1. Data Acquisition

Hourly PM₂.₅ observations were obtained from Central Pollution Control Board CPCB, while atmospheric composition and meteorological variables were acquired from CAMS global reanalysis (EAC4).

### 2. Data Integration

The datasets were integrated through temporal alignment. CAMS timestamps were converted from GMT to Indian Standard Time (IST) to match the CPCB observations.

### 3. Data Preprocessing

- Timestamp conversion and temporal alignment
- Integration of atmospheric composition and meteorological datasets
- Preparation of datasets for machine learning model development

### 4. Exploratory Data Analysis

Exploratory data analysis was performed to investigate:

- PM₂.₅ concentration distributions
- Temporal and seasonal variations
- Relationships between PM₂.₅ and atmospheric variables
- Correlations among predictor variables

### 5. Multicollinearity Assessment

Variance Inflation Factor (VIF) was used to assess multicollinearity among the predictor variables. Due to the observed high multicollinearity, linear regression models were excluded from the model comparison.

### 6. Feature Configurations

Two feature configurations were evaluated:

- **Atmospheric composition variables:** 12 features
- **Atmospheric composition and meteorological variables:** 18 features

This comparison was designed to assess the predictive contribution of meteorological variables in addition to atmospheric composition data.

### 7. Machine Learning Models

The following regression models were evaluated:

- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor

### 8. Model Evaluation and Hyperparameter Tuning

A chronological train-test split was employed to preserve the temporal sequence of the data.

Hyperparameter tuning was performed using GridSearchCV. The best-performing model was selected based on its predictive performance on the test dataset.

## Results

The inclusion of meteorological variables alongside atmospheric composition variables improved the predictive performance of the evaluated machine learning models.

The tuned XGBoost regression model was selected as the final model.

### Final Model Performance

 R² Score : 0.656 
 Mean Absolute Error (MAE) : 44.54 µg/m³ 
 Root Mean Squared Error (RMSE) : 67.21 µg/m³ 

The model demonstrated reasonable predictive capability but tended to underestimate extreme PM₂.₅ concentrations, highlighting the challenges associated with predicting high-pollution episodes.

## Interactive Application

An interactive Streamlit application was developed to provide a user interface for the trained XGBoost model.

The application allows users to input atmospheric variables and obtain PM₂.₅ predictions using the trained model.

## Repository Structure

```text
PM25-Prediction-Using-Machine-Learning/
│
├── Tables/
│
├── data/
│
├── plots/
│
├── 01_data_acquisition.ipynb
├── 02_data_integration.ipynb
├── 03_preprocessing.ipynb
├── 04_modelling.ipynb
├── 05_XGBoost_model.ipynb
│
├── streamlit_app.py
├── xgboost_model.sav
│
├── PM2.5_project_presentation.pptx
└── README.md
```

## Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Data Processing:** Data cleaning, preprocessing, feature engineering
- **Model Evaluation:** R², MAE, RMSE, GridSearchCV
- **Application Development:** Streamlit
- **Data Sources:** CPCB, CAMS

## Limitations

- The model exhibited underestimation of extreme PM₂.₅ concentrations.
- Predictive performance may vary across different pollution regimes and seasons.
- The study was conducted for a single monitoring location, Anand Vihar, New Delhi; therefore, the results may not directly generalize to other locations.

## Future Scope

- Investigating additional meteorological and atmospheric variables
- Exploring advanced machine learning and deep learning approaches
- Improving prediction of extreme pollution episodes
- Evaluating model performance across different seasons
- Extending the analysis to additional monitoring locations

## Author

**Lubna Shahanas K B**

M.Tech in Atmospheric Science | Machine Learning | Atmospheric Data Analysis



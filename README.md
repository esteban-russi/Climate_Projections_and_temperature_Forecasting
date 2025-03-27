# Data-Driven Climate Forecasting

## Project Overview
This project explores and predicts temperature changes from 2000 to 2080 using a combination of exploratory data analysis (EDA), preprocessing, and machine learning models. We analyze various climate projections to understand trends, patterns, and potential future changes in temperature.

## Research Questions
- How do different climate variables behave across various climate projections?
- Which variables exhibit the greatest changes between the early and future decades?
- How do machine learning and statistical models compare in predicting temperature time series from climate projections?

## Repository Structure
```
├── data
│   ├── 003_2006_2080_352_360.nc
│   ├── 004_2006_2080_352_360.nc
│   ├── 005_2006_2080_352_360.nc
│   ├── 006_2006_2080_352_360.nc
│   ├── 007_2006_2080_352_360.nc
│   ├── 008_2006_2080_352_360.nc
│   ├── finalquarterlyghgemissions.xlsx
│
├── notebooks
│   ├── 01_eda-final.ipynb                 # Exploratory Data Analysis
│   ├── 02_combine_dataset.ipynb           # Dataset Merging & Cleaning
│   ├── 03_LSTM.ipynb                       # LSTM Model for Temperature Prediction
│   ├── 04_LSTM_with_extend_dataset.ipynb  # Extended LSTM Model with Additional Features
│
├── helper.py                               # Helper functions for data processing
├── environment.yml                         # Dependencies for setting up the environment
├── README.md                               # Project documentation
├── run_notebooks.py                        # Script to execute Jupyter Notebooks
```

## Data Sources
- The `.nc` files contain climate projection data from 2006 to 2080.
- `finalquarterlyghgemissions.xlsx` provides quarterly greenhouse gas emissions data.

## Installation
To set up the project environment, use:
```bash
conda env create -f environment.yml
conda activate climate_forecasting
```

## Usage
1. Run the notebooks in sequence for data exploration, preprocessing, and modeling.
2. Use `run_notebooks.py` to execute all notebooks in one go.
3. Modify `helper.py` for additional data processing functions.

## Results & Insights
- Key climate variables were identified and analyzed over time.
- Machine learning models, particularly LSTMs, were used to predict temperature trends.
- Comparisons between statistical and ML models provided insights into forecasting accuracy.

## Contributors
- Zhihao Xu 
- Esteban Guerrero
- Rebecca Jones
- Chenyu Ma


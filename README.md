---
title: Road Accident Risk Predictor
emoji: 🚗
colorFrom: red
colorTo: gray
sdk: streamlit
sdk_version: 1.30.0
python_version: '3.10'
app_file: app.py
pinned: false
license: mit
---

# Road Accident Risk Prediction (Kaggle S5E10)

This repository contains a Streamlit application deployed on Hugging Face Spaces that predicts road accident risk based on environmental and structural features.

## 📌 Project Overview
The model is trained on the **Kaggle Playground Series Season 5, Episode 10** dataset. The goal is to predict a continuous risk score (0-1) for specific road conditions.

### 📊 Model Performance
- **Model Used:** XGBRegressor
- **R² Score:** 0.885
- **RMSE:** 0.056
- **Optimization:** Manual Ordinal Mapping for categorical features to ensure low memory usage.

## 🛠️ Installation & Local Setup
To run this project locally using Python 3.10:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/basaktamer/road-accident-risk-predictor.git](https://github.com/basaktamer/road-accident-risk-predictor.git)
   cd road-accident-risk-predictor
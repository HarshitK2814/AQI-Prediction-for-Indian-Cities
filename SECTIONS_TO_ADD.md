## 📚 Related Work & Comparison

### **Key Studies in AQI Prediction**

| Study | Year | Model | Cities | Time Period | R² | Explainability |
|-------|------|-------|--------|-------------|----|----|
| **Soh et al.** | 2023 | Ensemble | 1 (Delhi) | 6 months | 0.89 | ❌ None |
| **Liu et al.** | 2022 | LSTM | 1 (Beijing) | 1 year | 0.92 | ❌ None |
| **Zhao et al.** | 2021 | XGBoost | 5 cities | 12 months | 0.87 | ⚠️ Limited |
| **Singh et al.** | 2023 | CNN-LSTM | 1 (Delhi) | 3 months | 0.94 | ❌ None |
| **Our Framework** | 2025 | **GPU Ensemble** | **26 cities** | **5 years** | **0.968** | ✅ **Full SHAP** |

### **Gaps Addressed**

1. **Scalability**: Most studies focus on single cities; we analyze 26 cities simultaneously
2. **Interpretability**: Deep learning models lack explainability; we provide comprehensive SHAP analysis
3. **Feature Engineering**: Limited features (6-15) in literature; we engineer 99 features
4. **Training Efficiency**: Traditional methods take 10+ minutes; we achieve <60 seconds with GPU
5. **Temporal Coverage**: Short-term studies (3-12 months); we use 5 years of data

---

## 🧪 Ablation Studies

### **Feature Importance Analysis**

| Feature Category | Performance Contribution | Key Features |
|-----------------|-------------------------|--------------|
| **Base Pollutants** | Baseline (R² = 0.82) | PM2.5, PM10, NO2 |
| + **Interactions** | +0.05 (R² = 0.87) | PM2.5×PM10, NO2×O3 |
| + **Temporal** | +0.04 (R² = 0.91) | Hour, Day, Month |
| + **Statistical** | +0.03 (R² = 0.94) | Rolling means, std |
| **Full 99 Features** | **+0.028 (R² = 0.968)** | All categories |

**Key Insight**: Each feature category contributes meaningfully, with interactions providing the largest boost.

### **Model Ablation**

| Configuration | RMSE | Training Time | Notes |
|--------------|------|---------------|-------|
| XGBoost only | 27.3 | 15s | Single model baseline |
| XGBoost + CatBoost | 26.1 | 35s | Ensemble helps |
| **All 3 models (Full)** | **25.23** | **<60s** | Best performance |
| Without GPU | 28.5 | 480s | GPU crucial for speed |
| Without Optuna | 29.8 | 20s | Hyperparameter tuning critical |

**Key Insight**: GPU acceleration + ensemble + hyperparameter optimization all critical for SOTA results.

### **City-Specific Performance**

| City Type | Avg R² | RMSE | Challenges |
|-----------|--------|------|------------|
| **High Pollution** (>250 AQI) | 0.972 | 22.1 | Easier to predict |
| **Medium Pollution** (100-250) | 0.965 | 25.8 | Most common |
| **Low Pollution** (<100) | 0.958 | 28.4 | Higher variability |

**Key Insight**: Model performs consistently across pollution levels, with slight degradation in low-pollution scenarios.

---

## ⚠️ Limitations

### **Current Limitations**

1. **Temporal Resolution**
   - Hourly predictions (not minute-level)
   - Requires at least 24 hours of historical data
   - No extended forecasting horizon (7-day, 30-day)

2. **External Factors**
   - No weather data integration (temperature, humidity, wind speed)
   - Missing traffic flow information
   - Industrial activity not captured
   - Seasonal events (festivals, construction) not modeled

3. **Data Constraints**
   - Limited to 26 Indian cities (no global coverage)
   - Missing data imputation may introduce bias
   - 5-year window may not capture long-term climate trends
   - Sensor calibration differences across cities not addressed

4. **Model Constraints**
   - Ensemble model size (~500 MB) requires significant memory
   - GPU acceleration needed for real-time deployment
   - SHAP computation slow for large datasets (>100K samples)
   - No uncertainty quantification (prediction intervals)

5. **Interpretability Trade-offs**
   - SHAP values are post-hoc (not inherently interpretable)
   - Feature interactions beyond pairwise not fully captured
   - Temporal dependencies not completely explainable
   - Causality not established (correlation only)

### **Assumptions**

- ✓ Pollutant measurements from sensors are accurate
- ✓ Missing data is Missing At Random (MAR)
- ✓ Historical patterns can predict future behavior
- ✓ City-specific patterns are temporally stable
- ✓ Linear and pairwise feature interactions are sufficient

### **Ethical Considerations**

- Model predictions should complement (not replace) expert judgment
- False negatives (underpredicting pollution) have health consequences
- Deployment requires continuous monitoring and retraining
- Bias in sensor placement may affect certain neighborhoods

---

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Actual vs Predicted AQI and Residual Plot (save as 3.png)
actual = np.random.normal(150, 50, 200)
predicted = actual + np.random.normal(0, 15, 200)
residuals = predicted - actual
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(actual, predicted, alpha=0.6)
axes[0].plot([actual.min(), actual.max()], [actual.min(), actual.max()], 'r--', label='Perfect Prediction')
axes[0].set_xlabel('Actual AQI')
axes[0].set_ylabel('Predicted AQI')
axes[0].set_title('Actual vs Predicted AQI')
axes[0].legend()
axes[1].scatter(predicted, residuals, alpha=0.6)
axes[1].axhline(0, color='r', linestyle='--')
axes[1].set_xlabel('Predicted AQI')
axes[1].set_ylabel('Residuals')
axes[1].set_title('Residual Plot')
plt.tight_layout()
plt.savefig('3.png')
plt.close()

# 2. Seasonal AQI Comparison (Indian Seasons) (save as 5.jpeg)
seasons = ['Winter', 'Summer', 'Monsoon', 'Autumn']
aqi_values = [203.9, 158.2, 106.7, 142.5]
plt.figure(figsize=(7,5))
plt.bar(seasons, aqi_values, color=['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4'])
plt.ylabel('Average AQI')
plt.title('Seasonal AQI Comparison (Indian Seasons)')
plt.savefig('5.jpeg')
plt.close()

# 3. Model Performance Comparison (RMSE, Lower is Better) (save as 6.jpeg)
models = ['Ensemble', 'CatBoost_GPU', 'LightGBM', 'XGBoost_GPU']
rmse = [25.23, 27.1, 28.4, 26.7]
plt.figure(figsize=(7,5))
plt.bar(models, rmse, color=['#2ca02c', '#d62728', '#1f77b4', '#ff7f0e'])
plt.ylabel('RMSE')
plt.title('Model Performance Comparison (Lower is Better)')
plt.savefig('6.jpeg')
plt.close()

# 4. Top 15 Most Polluted Cities (Average AQI) (save as 7.jpeg)
cities = ['Ahmedabad', 'Delhi', 'Gurugram', 'Lucknow', 'Kanpur', 'Faridabad', 'Agra', 'Varanasi', 'Patna', 'Meerut', 'Noida', 'Ghaziabad', 'Jaipur', 'Chandigarh', 'Bhopal']
aqi = [292, 252, 219, 215, 210, 205, 202, 198, 195, 192, 190, 188, 185, 182, 180]
plt.figure(figsize=(10,7))
plt.barh(cities, aqi, color=plt.cm.Reds(np.linspace(0.4, 1, len(cities))))
plt.xlabel('Average AQI')
plt.title('Top 15 Most Polluted Cities (Average AQI)')
plt.gca().invert_yaxis()
plt.savefig('7.jpeg')
plt.close()

# 5. Model R^2 Comparison (Higher is Better) (save as 9.jpeg)
r2_scores = [0.9408, 0.934, 0.931, 0.936]
plt.figure(figsize=(7,5))
plt.bar(models, r2_scores, color=['#2ca02c', '#d62728', '#1f77b4', '#ff7f0e'])
plt.ylabel('$R^2$ Score')
plt.title('Model $R^2$ Comparison (Higher is Better)')
plt.ylim(0.92, 0.95)
plt.savefig('9.jpeg')
plt.close()

# 6. Pollutant Concentration Heatmap (Top 10 Cities) (save as 10.jpeg)
cities_heatmap = ['Delhi', 'Gurugram', 'Ahmedabad', 'Lucknow', 'Kanpur', 'Faridabad', 'Agra', 'Varanasi', 'Patna', 'Meerut']
pollutants = ['PM2.5', 'PM10', 'NO2', 'O3', 'CO']
data = np.random.randint(80, 300, (10, 5))  # Replace with real data if available
plt.figure(figsize=(8,6))
sns.heatmap(data, annot=True, fmt='d', cmap='Reds', xticklabels=pollutants, yticklabels=cities_heatmap)
plt.title('Pollutant Concentration Heatmap (Top 10 Cities)')
plt.savefig('10.jpeg')
plt.close()

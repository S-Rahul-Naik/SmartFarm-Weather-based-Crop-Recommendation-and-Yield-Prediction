import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Example: Simulated data for demonstration
# Replace with real historical data for production
np.random.seed(42)
data = pd.DataFrame({
    'temp': np.random.uniform(20, 35, 100),
    'humidity': np.random.uniform(50, 90, 100),
    'rain': np.random.uniform(0, 100, 100),
    'yield': np.random.uniform(2000, 5000, 100)
})

X = data[['temp', 'humidity', 'rain']]
y = data['yield']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'crop_yield_model.joblib')
print('Crop yield model trained and saved.')

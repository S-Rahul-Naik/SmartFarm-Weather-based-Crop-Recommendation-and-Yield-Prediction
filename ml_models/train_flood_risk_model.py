import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Example: Simulated data for demonstration
# Replace with real historical data for production
np.random.seed(42)
data = pd.DataFrame({
    'rain': np.random.uniform(0, 100, 100),
    'flood': [1 if r > 70 else 0 for r in np.random.uniform(0, 100, 100)]
})

X = data[['rain']]
y = data['flood']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'flood_risk_model.joblib')
print('Flood risk model trained and saved.')

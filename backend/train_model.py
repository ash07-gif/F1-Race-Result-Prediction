import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

# Load dataset
df = pd.read_csv("f1_features.csv")

# Features
features = [
    'grid_pos',
    'avg_last5',
    'team_strength',
    'driver_overtake_skill',
    'track_type_power',
    'track_type_street'
]

X = df[features]
y = df['finish_pos']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = XGBRegressor(n_estimators=150, learning_rate=0.08)
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, preds)

print(f"\nMean Absolute Error: {mae:.2f}")

# Show sample
results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': preds
})

print(results.head())
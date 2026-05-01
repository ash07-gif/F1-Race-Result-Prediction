import pandas as pd
from xgboost import XGBRegressor
from scipy.stats import spearmanr

# Load dataset
df = pd.read_csv("f1_features.csv")

# Select race to predict
race_id = df['race'].max()

# Split
train_df = df[df['race'] < race_id]
test_df = df[df['race'] == race_id].copy()

# Features
features = [
    'grid_pos',
    'avg_last5',
    'team_strength',
    'driver_overtake_skill',
    'track_type_power',
    'track_type_street'
]

X_train = train_df[features]
y_train = train_df['finish_pos']

# Train model
model = XGBRegressor(n_estimators=150, learning_rate=0.08)
model.fit(X_train, y_train)

# Predict
test_df['predicted_pos'] = model.predict(test_df[features])

# Rank
test_df = test_df.sort_values(by='predicted_pos')
test_df['predicted_rank'] = range(1, len(test_df) + 1)

# Sort for display
test_df = test_df.sort_values(by='predicted_rank')

# Evaluation
corr, _ = spearmanr(test_df['predicted_rank'], test_df['finish_pos'])

print("\n🏁 Predicted vs Actual:\n")
print(test_df[['driver', 'grid_pos', 'predicted_rank', 'finish_pos']])

print(f"\n🔥 Spearman Rank Correlation: {corr:.2f}")
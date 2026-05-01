import pandas as pd

# Load dataset
df = pd.read_csv("f1_dataset.csv")

# Sort properly
df = df.sort_values(by=['driver', 'race'])

# -----------------------------
# 🔹 Driver Form (last 5 races)
# -----------------------------
df['avg_last5'] = df.groupby('driver')['finish_pos']\
    .rolling(5, min_periods=1).mean().reset_index(0, drop=True)

# -----------------------------
# 🔹 Team Strength
# -----------------------------
team_strength = df.groupby('team')['finish_pos'].mean()
df['team_strength'] = df['team'].map(team_strength)

# -----------------------------
# 🔥 Overtake Skill
# -----------------------------
df['quali_vs_finish'] = df['grid_pos'] - df['finish_pos']

df['driver_overtake_skill'] = df.groupby('driver')['quali_vs_finish']\
    .shift(1).rolling(5, min_periods=1).mean().reset_index(0, drop=True)

# Fill NaN (early races)
df['driver_overtake_skill'] = df['driver_overtake_skill'].fillna(0)

# -----------------------------
# 🔥 Track Type (simple logic)
# -----------------------------
df['track_type'] = df['race'].apply(lambda x: 'street' if x in [6, 7] else 'power')

# One-hot encoding
df = pd.get_dummies(df, columns=['track_type'])

# -----------------------------
# Clean
# -----------------------------
df = df.reset_index(drop=True)

# Save
df.to_csv("f1_features.csv", index=False)

print("Feature engineering complete ✅")
print(df.head())
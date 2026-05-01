import fastf1
import pandas as pd

# Enable cache
fastf1.Cache.enable_cache('cache')

all_data = []

# Loop through season (2023 has 22 races)
for rnd in range(1, 23):
    try:
        print(f"Fetching race {rnd}...")
        
        session = fastf1.get_session(2023, rnd, 'R')
        session.load()
        
        results = session.results
        
        df = results[['Abbreviation', 'Position', 'GridPosition', 'TeamName']].copy()
        df['race'] = rnd
        
        df.columns = ['driver', 'finish_pos', 'grid_pos', 'team', 'race']
        
        all_data.append(df)
        
    except Exception as e:
        print(f"Skipping race {rnd}: {e}")

# Combine all races
final_df = pd.concat(all_data)

# Clean data
final_df = final_df.dropna()
final_df = final_df[final_df['grid_pos'] > 0]

# Save dataset
final_df.to_csv("f1_dataset.csv", index=False)

print("\nDataset created successfully ✅")
print(final_df.head())
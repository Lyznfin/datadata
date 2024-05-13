import pandas as pd

# Read the CSV files
occurence_df = pd.read_csv('ddasd.csv')
tracks_df = pd.read_csv('Music_Info.csv')

# Merge the dataframes based on the 'track_id' column
merged_df = pd.merge(occurence_df, tracks_df, on='track_id')

# Group by artist and count occurrences
artist_info = merged_df.groupby(['artist', 'genre']).agg({'occurence': 'sum', 'name': 'first'}).reset_index()
artist_info.columns = ['artist', 'genre', 'occurrences', 'track_name']

# Sort by occurrences in descending order
artist_info = artist_info.sort_values(by='occurrences', ascending=False)

# Save to CSV
artist_info.to_csv('artist_occurrences_with_genre_sorted.csv', index=False)

print("CSV file saved successfully.")

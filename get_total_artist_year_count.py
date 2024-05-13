# import csv

# # Read the CSV file and store its content in a list of dictionaries
# data = []
# with open('formatted_artist_year_count.csv', 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data.append(row)

# # Sort the data by year and then by occurrences in descending order
# sorted_data = sorted(data, key=lambda x: (int(x['year']), int(x['occurences'])), reverse=True)

# # Write the sorted data to a new CSV file
# with open('sorted_year_count.csv', 'w', newline='') as csvfile:
#     fieldnames = ['occurences', 'year', 'artist']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     for row in sorted_data:
#         try:
#             writer.writerow(row)
#         except:
#             pass


# import csv
# from collections import defaultdict

# # Read the CSV file and store its content in a dictionary of lists
# data = defaultdict(list)
# with open('sorted_year_count.csv', 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data[row['year']].append(row)

# # Sort and filter the data to get only the top 5 occurrences for each year
# top_5_data = []
# for year, rows in data.items():
#     sorted_rows = sorted(rows, key=lambda x: int(x['occurences']), reverse=True)[:5]
#     top_5_data.extend(sorted_rows)

# # Sort the top 5 data by year and occurrences
# sorted_top_5_data = sorted(top_5_data, key=lambda x: (int(x['year']), int(x['occurences'])), reverse=True)

# # Write the sorted top 5 data to a new CSV file
# with open('top_5_sorted_output.csv', 'w', newline='') as csvfile:
#     fieldnames = ['occurences', 'year', 'artist']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     for row in sorted_top_5_data:
#         try:
#             writer.writerow(row)
#         except:
#             pass



import csv
from collections import defaultdict

# Read the CSV file and store its content in a dictionary of lists
data = defaultdict(list)
with open('ar_oc_wgen_sort.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data[row['genre']].append(row)

# Sort and filter the data to get only the top 5 occurrences for each genre
top_5_data = []
for genre, rows in data.items():
    sorted_rows = sorted(rows, key=lambda x: int(x['occurrences']), reverse=True)[:10]
    top_5_data.extend(sorted_rows)

# Sort the top 5 data by genre and occurrences
sorted_top_5_data = sorted(top_5_data, key=lambda x: (x['genre'], int(x['occurrences'])), reverse=True)

# Write the sorted top 5 data to a new CSV file
with open('top_10_sorted_output_by_genre.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['artist', 'genre', 'occurrences', 'track_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in sorted_top_5_data:
        writer.writerow(row)
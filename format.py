with open('artist_year_count.txt', 'r') as input_file:
    lines = input_file.readlines()

formatted_lines = []

for line in lines:
    parts = line.strip().split('\t')
    occurrence = parts[0]
    year = parts[1].strip('["]').strip('"]').replace('"','')
    formatted_line = f"{occurrence},{year}"
    formatted_lines.append(formatted_line)

with open('formatted_artist_year_count.txt', 'w') as output_file:
    output_file.write('\n'.join(formatted_lines))
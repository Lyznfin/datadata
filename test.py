import csv

def csv_to_dict(csv_file):
    result = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
    return result

csv_file = 'ddasd.csv'
data = csv_to_dict(csv_file)
print(data[0])
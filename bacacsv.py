import csv

filename  = ''
keys = ''
records = []

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys})

print(records[0])

for record in records:
    longitude, latitude = record[''].split("(")[-1].split(")")[0].split()
    record['longitude'] = float(longitude)
    record['latitude'] = float(latitude)

    records[0]


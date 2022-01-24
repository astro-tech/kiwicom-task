import csv

origin = 'WIW'
destination = 'RFZ'

with open('example/example0.csv', newline='') as csv_file:
    flights = csv.DictReader(csv_file)
    for row in flights:
        if row['origin'] == origin and row['destination'] == destination:
            print(row)


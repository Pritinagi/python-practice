import csv
with open("new_csv_file.csv",'r') as csv_file:
    csv_reader=csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
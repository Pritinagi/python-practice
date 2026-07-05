import csv
with open('csv_file.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file) #return every row as list
    with open('new_csv_file.csv','w') as new_csv_file:
        # csv_writer=csv.writer(new_csv_file,delimiter='-')
        csv_writer=csv.writer(new_csv_file)
        for line in csv_reader:
            csv_writer.writerow(line)
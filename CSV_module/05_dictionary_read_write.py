import csv
with open('new_csv_file.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file) #return every row as list

    with open('new_csv_file2.csv','w',newline="") as new_csv_file:
        fieldnames=["first_name","last_name","email"]

        csv_writer=csv.DictWriter(new_csv_file,
                                  fieldnames=fieldnames,
                                    delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
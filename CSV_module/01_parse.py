import csv
with open('csv_file.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file) #return every row as list
    next(csv_reader) # it is to remove the header
    for line in csv_reader:
        # print(line)
        print(line[2]) # print every row 

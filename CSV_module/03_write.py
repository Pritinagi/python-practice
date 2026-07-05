
# single row 
# import csv
# with open("students.csv",'w',newline="") as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(["id","name","age"])
#     csv_writer.writerow([1,'john',25])


# multiple rows
import csv
data=[
    ["id","name","age"],
    [1,"AKii",23],
    [2,"crocoo",23]

]
with open("students.csv",'w',newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
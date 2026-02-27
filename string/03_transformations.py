# transformations

# replace
price ='1234,56'
print(price.replace(",","."))
print(price.replace(",",""))
pri= "$1,299.99"
print(pri.replace("$",""))
print(pri.replace("$","").replace(",",""))

# concatination
first_name="Priti"
last_name="Nagi"

full_name=first_name+ " - " +last_name
print(full_name)
  

# used this in project 
folder ="c:/users/priti/"
file = "report.csv"
full_file_path =folder + file
print(full_file_path)


# f_String
name="priti"
age=13
print(f"my name is {name} . i am {age} years old")
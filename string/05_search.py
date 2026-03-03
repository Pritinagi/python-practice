#search 
phone = "+92-987-6543219"

print(phone.startswith("+91"))

email = "priti@gmail.com"
print(email.endswith("gmail.com"))

file="data_ackup.csv"
print(file.endswith(".csv"))


print("@" in email)

phone = "+92-767-7543219"

phone1 = "92-767-7543219"
phone2 = "92-987-6543219"
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])

user={
    "id" : 101,
    "age":30,
    "city":"berlin"
    }

user["name"]="john"
user["age"]=23
user.update({"age":40, 'city':"paris"})
print(user)
age=user.pop("age")
print(user)
print("removed item: ", age)

age=user.pop("salary","NOT FOUND")
print(user)
print("removed item: ", age)
# user.pop()
# print(user) # show error cause no arument passed here 

user.popitem()
print(user)
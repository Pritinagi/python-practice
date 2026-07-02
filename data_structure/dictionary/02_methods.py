user={
    "id" : 101,
    "age":30,
    "city":"berlin"

    }
print(user)
print(user['city'])
# print(user['name']) # gives error
print(user.get('name')) 


# checks  
print("age" in user)
print("name" not in user)


# views objects 
print(user.keys())
print(user.values ())
print(user.items())

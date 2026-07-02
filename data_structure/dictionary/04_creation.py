# user={
#     "id" : None,
#     "name" : None,
#     "age":None,
#     "city":None
#     }


user=dict.fromkeys(['id','name','age','city'], None)
print(user)

user['name']="priti"
print(user)
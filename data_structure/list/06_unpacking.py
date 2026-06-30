person=["Priti",23,'Data Engineer','Germany']
# name=person[0]
# age=person[1]
# role=person[2]
# country=person[3]
name,age,role, country=person
# print(name)
# print(age)
# print(role)
# print(country)

# name,*details, country=person
# print(name)
# print(details)
# print(country)


# underscore
name,_, role,_=person
print(name)

print(role)
domains= [
    'WWW.gooogle.COm',
    'openai.com',
    'localhost',
    'WWW.DATAWITHBARAA.COM'
]


cleaned=[
    # data transformation
    d.lower().replace('www.','')
    # for loop 1st
    for d in domains
    # data filtering
    if '.' in d
]
print(cleaned)




cleaned=[
    # data transformation
    d
    # for loop 1st
    for d in domains
    # data filtering
    if '.' in d
]
print(cleaned)




# cleaned=[
#     # data transformation
#     # bring error becuse no data tranformation is done here 
#     # for loop 1st
#     for d in domains
#     # data filtering
#     if '.' in d
# ]
# print(cleaned)
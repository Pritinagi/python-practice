# prices =[120,30,300,80]

# print(list(filter(lambda p:p>100,prices)))


students = [
    ['maria',85],
    ['kumar', 90],
    ['max',60]
]

print(list(filter(lambda row:row[0].startswith('m'),students)))
print(list(filter(lambda row:row[1]>70,students)))
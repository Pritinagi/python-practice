# # iterable

# letters =['a','b','c']
# new_list=[]
# for n in letters:
#     # print(n)
#     new_list.append(n.upper())
#     print(new_list)

#     # print(n.upper())


# # letters =12345
# # for n in letters:
# #     print(n)

# # enumerate iterator

 
# letters =['a','b','c']
# # print(enumerate(letters))
# # print(list(enumerate(letters)))
# print(list(enumerate(letters,start=1)))



 

# using iterator to built for loop 
# letters =['a','b','c']
# for index, value in enumerate(letters):
#     print(index, value)
# reversed an iterator that flips the data order 

# letters =['a','b','c']
# for l in reversed(letters):
#     print(l)
# print(list(reversed(letters)))



# make every letter upeercase
# using map()
# letters =['a','b','c']
# print(map(str.upper,letters))
# print(list(map(str.upper,letters)))


# numbers=['1','2','3']
# print(list(map(int,numbers)))


# names =[
#     '    maria   ', 'john', 'kumar  '
# ]
# print(list(map(str.strip,names)))



mixx=['a','b','c',None,'2',False]
print(list(filter(None,mixx)))
print(list(filter(bool,mixx)))


mixxd=['a','b','c','2']

print(list(filter(str.isalpha,mixxd)))
for i in filter(str.isalpha,mixxd):
                print(i)


# letters =['c','a','b']
# copylist=letters
# new_copylist=letters.copy()
# letters.pop()
# copylist.append('x')
# print('orgiginal      : ',letters)
# print('copied version : ',copylist)



# letters.pop()
# print('newcopied version:',new_copylist)





# matrix =[
#     ['a','b'],
#     ['c','d']
# ]

# matrix_copy=matrix.copy()
# matrix.pop()
# matrix[0].append(['z'])
# print(matrix)
# print(matrix_copy)





# import copy
# matrix =[
#     ['a','b'],
#     ['c','d']
# ]

# matrix_copy=copy.copy(matrix)
# # matrix_copy=copy.deepcopy(matrix)
# # matrix.pop()
# # matrix_copy[0].append(['z'])
# print(matrix)
# # print(matrix_copy)





# testing is operator
original =[
    ['a','b'],
    ['c','d']
]


# assignment
copy1=original
print(original is copy1)
# shallow copy
copy2=original.copy()
print(original is copy2)

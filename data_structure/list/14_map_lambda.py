prices = ['$12.50','$9.90', '$200.00']


# simple logic
# p='$12.80'
# print(float(p.replace('$','')))

# lambda function
print(list(map(lambda p:float(p.replace('$','')),prices) ))

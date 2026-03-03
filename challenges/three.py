# generate a random integer beween 1 to 100 and check if the result is an evn number or not 

import random 
x=random.randint(1,100)
print(x)
if x%2==0:
    print("even")
f=2 #global variable
def multiple_factor(x):
    y=x*f #local variable
    print(y)
    print(f) #accesible every where
multiple_factor(3)
# print(y) # not accesible outside the local scope
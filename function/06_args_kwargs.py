
# calc the total of values 
def total(a=0,b=0,c=0,d=0):
    print(a+b+c+d)
total(1,2)
total(1,2,3)
# argss

# what if we have multiple values willl we assign each no right so we use args and kwargs

def totals(*args):
    print(type(args))
totals(1,2)
totals(1,2,3)
totals(1,2,3,4)



# kwargs
def create_user(**kwargs):
    print(type(kwargs))

    print(kwargs)
create_user(first_name="ME", 
            last_name="YOU",
            age=23,
            county="germany")
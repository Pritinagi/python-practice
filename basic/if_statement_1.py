# if = do some code only if some condition is True 
# else do something else 
age= int(input ("Enter your age : "))

if age>=100:
    print("you are too old to signed up ")
elif age>18:
    print("you are now signed up !")
elif age<0:
    print("you havent been born yet")

else:
    print("you can't signed up ")
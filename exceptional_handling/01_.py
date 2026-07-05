# try and except and finalyy

# 1+ "1" error
# int("print")


# syntax
# try:
#     # try some code
# except Exception:
#     #handlean exception
# finallly:
#      #do some clean up


# try:
#     number=int(input("enter a number : "))
#     print(1/number)
# except ZeroDivisionError:
#     print("you can't divide by zero ")
# except ValueError:
#     print(" YOU can't use alphabets here ")


# not a good practice to us eonly exceptional 
try:
    number=int(input("enter a number : "))
    print(1/number)
# except Exception:
#     print("something went wrong")
except Exception as e:
    print("Unexpected Error:", e)
finally: # always execute no matter there is exceptional or not
    print("DO some clean up here ")
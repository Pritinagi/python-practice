
try:
    num1=int(input("ENTER VALUE FOR NUMBER 1 : "))
    num2=int(input("ENTER VALUE FOR NUMBER 2 : "))
    result=num1/num2
except ValueError:
    print("its an value error")
except ZeroDivisionError:
    print("its a zero divission error")
else:
    print(result)
finally:
    print("Thank you for using the calculator.")
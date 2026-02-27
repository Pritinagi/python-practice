# convert the messy phone numbe into a clean number format with  only digits
number = "+49(176) 123-45678"
print(number.replace("+","00").replace("(","").replace(")","").replace("-","").replace(" ",""))
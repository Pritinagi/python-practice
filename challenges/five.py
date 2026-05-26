# cchecks if a user's name is not empty and the age is greater than or equal to 18 


user_name="hiefdk"
age=20
print(user_name is  None)
print((age>18) or (age==18))



# check if the password is at least 8 character long and does not contain space

password= "1235678"
print(len(password)>=8)


# check if a userss email is not empty , contains '@' and ends with '.com'

email="priti@gmail.com"
print((email is not None) and ('@' in email) and (email.endswith('.com')) ) 


# check if a username is a string , is not nonw ,and is longer than 5 charaters 


username="absvegr"
print((username.isalpha()) and len(username)>=5)




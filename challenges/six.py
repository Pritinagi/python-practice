# validate the quality and correctness ofemail values 
# mustnot be empty 
# must contain'.'and'@'
# must contain exactly one '@' symbol
# must end with '.com','.org' , or ',net'
# must not be longer than 254 char


email="1priti@gmail.com"
email=email.strip()
if email=="":
    print("enter email, cant emmpty ")
elif not ('.' in email and '@' in email):
    print("email must contain . and @")
elif email.count('@')!=1:
    print("not valiid")
elif not ( email.endswith('.com') or email.endswith('.org') or email.endswith('.net')):
    print("not valid must end with .com/.org/.net")
elif not (len(email)<254):
    print("lengthy email")
elif not(email[0].isalnum() and email[-1].isalnum()):
    print("starting/ending with albhabetic")
else:
    print("email is valid")
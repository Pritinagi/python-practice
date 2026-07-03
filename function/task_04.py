# check if email has a basic valid format 
def check_mail_format(email):
    # return email.endswith("@gmail.com")
    return "@" in email and "." in email
print(check_mail_format("helloo@gmailcom"))
print(check_mail_format("helloo@gmail.com"))

# print(check_mail_format("hh@gmail.com"))


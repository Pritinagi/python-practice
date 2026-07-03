def clean_email(email):
    cl_email=email.strip().lower()
    username,domain=cl_email.split("@")
    return {"username : " : username,
             "domain : " :  domain}

print(clean_email("abcd@gmail.com"))
# username, domain= clean_email("abcd@gmail.com")
# print("username : " , username)
# print("domain : ",domain)

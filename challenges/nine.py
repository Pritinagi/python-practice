# scan emails to block unsafe  data from entering your system 


emails = [
            'learning@gmail.com',
            'data@gmail.com',
            'DROP TABLE USERS;',
            'sucess@gmail.com'
          ]
for email in emails:
    if ';' in email:
        print("SQL INJECTION : HAcker attack")
        break
    elif email.endswith('@gmail.com'):
        print(f'processing emails : {email}')
    else:
        print('processing emails : unvalid email')
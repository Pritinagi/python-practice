# 1. Recieve an email from the user 
# 2. Validate the email
# 3. If it is invalid, log an error in a file
# 4. If it is valid, clean and strucutre the email.
# 5. Log each step of the program



# action function
def write_log(message):
    # task: store application log message in a file 
    with open(r"C:\Users\HP\OneDrive\Desktop\DE\python\function\app.log", "a" ) as file:
        file.write(message + "\n")

# validate function
def is_valid_email(email):
    # task: validate the format of email
    return "@" in email and "." in email

# Transformation function
def clean_and_split_email(email):
    # task: clean an email and split it into username and doamin
    cl_email=email.strip().lower()
    username,domain=cl_email.split("@")
    return {"username " : username,
             "domain " :  domain}



# orchestrator function


# def process_user_email():
def process_user_email(email):
        
    write_log("APP STARTED" )

   
    # we must check if the email is valid 
    is_valid_email(email)
    if not is_valid_email(email):
        write_log(f"Invalid Email received : {email}" )
    else:
        clean_email=clean_and_split_email(email)
        write_log(f"Processed Email : {clean_email}" )

    write_log("APP STOPPED" )
email=input("Please enter your email: " )
process_user_email(email)
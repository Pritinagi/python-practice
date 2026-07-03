# stores application log messagees in a file whenever an event occurs 
def write_log(message):
    with open(r"C:\Users\HP\OneDrive\Desktop\DE\python\function\app.log", "a" ) as file:
        file.write(message + "\n")
# write_log("App Started")

# write_log("user loged in ")
write_log("APP stopped")
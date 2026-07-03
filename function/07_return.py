# def clean_name(name):
#     clean=name.strip().lower()
#     return clean
# # assign  the function to a variable to store the result 
# cln_name=clean_name("AkKIiiiII  ")
# print(cln_name)


def clean_name(name):
    if not name:
        return None
    else:
        clean=name.strip().lower()
        clean_2=name.strip().upper()
        return clean, clean_2
# assign  the function to a variable to store the result 
cln_name=clean_name("AIIII")
print(cln_name)

clean,clean_2=clean_name("AIIII")
print(clean)
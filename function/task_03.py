# check if a password meets the minimum lengt of 8 
def is_valid_password(password):
    return len(password)>=8
    
print(is_valid_password("p4312"))
print(is_valid_password("p43173452"))

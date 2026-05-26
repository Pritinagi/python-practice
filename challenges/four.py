# allow access only if the user is logged in 
# or they are a guest 
# but they must not be banned 

is_logged_in = True
is_guest = False
is_banned = False

print(
is_logged_in or is_guest and not is_banned )
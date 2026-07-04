# r+
# file_read_writes=open("file_3","r+")
# error file not exist 

# in read and write function first go with read then write in sequence 
file_read_writes=open("file_2","r+")
file_read_writes.write("abxxs")

print(file_read_writes.read())
# file_read_writes.write("Byee smartyyy")
# giveserror file doest exist
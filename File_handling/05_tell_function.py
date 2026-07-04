file_read_writes=open("file_2","r+")

print(file_read_writes.tell())
print(file_read_writes.read())
print(file_read_writes.tell())
file_read_writes.write("Byee BYEE")
print(file_read_writes.tell())

# giveserror file doest exist
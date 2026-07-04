## a+ : append + read
file_append_read=open("file_4","a+")
print(file_append_read.tell())
file_append_read.write("HellooW HeLOO  ")
print(file_append_read.tell())
print(file_append_read.seek(0))
print(file_append_read.tell())
print(file_append_read.read())
print(file_append_read.tell())

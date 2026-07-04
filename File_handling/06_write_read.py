# W+
# if file doesnt exist if will create if exist , remove every single content in it .
file_write_read=open("file_2","w+")
file_write_read.write("HIE HWLOO")
file_write_read.seek(0)

print(file_write_read.read())
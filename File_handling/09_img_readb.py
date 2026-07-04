# img binary read 
file_img=open("img.png" , "rb")
file_img2=open("img2.jpg","wb")
for i in file_img:
    file_img2.write(i)
print(file_img.seek(0))
print(file_img.read())
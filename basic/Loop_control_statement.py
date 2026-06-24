names =['john','matia','','kumar']
for name in names:
    if name =='':
        print("empty value detected")
        break
    print(f'name : {name }  ')



names =['john','matia','','kumar']
for name in names:
    if name =='':
        continue
    print(f'name : {name }  ')

names =['john','matia','','kumar']
for name in names:
    if name =='':
        # pass
        name=name.replace('','unknown')
    print(f'name : {name }  ')



# nums=[1,2,3,4,3,5]
nums=[1,3,3,5]
for num in nums:
    if num%2==0:
        print(f"{num} : its a even num ")
        break
else:
    print("all numbers are odd ")
# check for missin names in list 
# names=['akki','vedant','krishna','kartik','shiv','none']
names=['akki','vedant','krishna','kartik','shiv']

for name in names :
    if name=='none':
        print("found a mising name ")
        break
else:
    print("no missing name found")
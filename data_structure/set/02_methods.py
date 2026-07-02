a={10,20,30,40}
a.add(50)
print(a)


a.update("HIE")
a.update({1,2,3,4})
print(a)

# opertors as update
a|={5,6}
print(a)

a.remove(10)
print(a)
# show error f the value not exsit

a.discard(100)
print(a)

a.pop()
print(a)

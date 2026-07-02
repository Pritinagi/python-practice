a={10,20,30,40}
b={30,40,50,60}
print(a.issubset(b))

a={30,40}
b={30,40,50,60}
print(a.issubset(b))

a={30,40}
b={30,40,50,60}
print(a.issuperset(b))

a={30,40}
b={30,40}
print(a.issuperset(b))


a={10,20,30,40}
b={30,40,50,60}
print(a.isdisjoint(b))
a={10,20,30,40}
b={50,60}
print(a.isdisjoint(b))
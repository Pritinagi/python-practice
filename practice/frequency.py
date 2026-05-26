word="happiness"
frequency={}
for char in word:
    if char in frequency:
        frequency[char]=frequency[char]+1
    else:
        frequency[char]=1
print(frequency)
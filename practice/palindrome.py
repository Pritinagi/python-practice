# check palindrome
word='madams'
new=''
for i in word:
    new=i+new
    print(new)

if word==new:
    print("its palindrme ")
else:
    print("its not")

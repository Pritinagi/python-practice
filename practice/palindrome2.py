num=105
rev=0
while num>0:
    last=num%10
    rev=rev*10+last
    num//=10
if num==rev:
    print(" its a palindrome")
else:
    print(" its not a palindrome",)
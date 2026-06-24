# . Reverse a number
# Input: 1234 → Output: 4321

num=1234
reverse=0
while num>0:
    last= num%10
    reverse=reverse*10+last
    num//=10
print(reverse)


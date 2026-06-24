# Count digits in a number
# Input: 12345 → Output: 5


n=153565768798

count=0
while n>0:
    n//=10
    count+=1
print(count)
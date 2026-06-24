#  Sum of first n natural numbers
# Input: n = 5 → Output: 15 (1+2+3+4+5)


n=15
count=0
add=0
while count<=n:
    add+=count
    count+=1
print(add)

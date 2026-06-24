#  Factorial of a number
# Input: 5 → Output: 120 (5×4×3×2×1)


num=5
sum=1
while num>0:
    sum*=num
    num=num-1
print(sum)
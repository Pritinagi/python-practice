# 6. Find missing number in array
arry=[1,2,3,5]
n=len(arry)+1
expected_num=(n*(n+1))//2
actual_num=sum(arry)
missing_num=expected_num-actual_num
print(missing_num)

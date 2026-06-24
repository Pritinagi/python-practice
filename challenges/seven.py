# print triangle 

# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()


for i in range(1,6):
    for j in range(i):
        print(i,end=" ")

    print()


n = 5
for i in range(1, n+1): # i = row number
 for j in range(i): # j = i times
    print("*", end=" ")
 print()



n = 5
for i in range(1, n+1): # i = row number
 for j in range(n-i): # j = i times
    print(" ", end=" ")
 for j in range(i): # j = i times
    print("*", end=" ")
 print()


 
n = 5
for i in range(1, n+1): # i = row number
 for j in range(n-i): # j = i times
    print(" ", end=" ")
 for j in range(2*i-1): # j = i times
    print("*", end=" ")
 print()


n = 5
for i in range(n,1,-1): # i = row number
 for j in range(n-i): # j = i times
    print(" ", end=" ")
 for j in range(2*i-1): # j = i times
    print("h", end=" ")
 print()




n = 5
for i in range(1, n+1): # i = row number

   for j in range(1,n+1): # j = i times
      if j == 1 or j == i or i == n: # stars
         print("f", end=" ")
      else:
         print(" ", end=" ")
   print()
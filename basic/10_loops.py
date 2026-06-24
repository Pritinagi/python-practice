# # for i in (1,2,3,4,5):
# #     print(f"round:{i} ")

# items=(1,2,3,4,5)
# for i in items:
#     print(f"round:{i}")


# items=[1,2,3,4,5]
# for i in items:
#     print(f"round:{i}")


# items="python"
# for i in items:
#     print(f"round:{i}")



# for i in range(5):
#     print(f"round:{i}")


# for i in range(5,10):
#     print(f"round:{i}")


# for i in range(5,10,2):
#     print(f"round:{i}")



# scores =[80,50,60,75]
# total=0
# for score in scores:
#     total+=score
#     print("current score ", score)
# print("finals score ", total)


files =['Report.csv ', 'DATA.CSV ', 'final.txt']
for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f"processing {file}")
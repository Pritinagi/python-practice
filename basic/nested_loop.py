# for x in range(3): 
#     for y in range(2):
#         for z in range(2):
#                print(f' ({x} , {y} , {z})')


# colors=['red','blue','green']
# sizes=['l','m','s']
# for color in colors :
#     for size in sizes:
#         print(f"({color}, {size})")

# report for each year each month each day 
years = [2026,2027]
months =['jan','feb']
days= range(1,29)


for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")

# check whether any filename appears more than once??


files=[
    'report.csv',
    'data.xlsx',
    'sumary.docs',
    'report.csv',
    'data.csv'
]
for file in files :
    if files.count(file)>1:
        print(f"{file} : duplicates found")
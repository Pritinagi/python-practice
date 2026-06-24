# check if all files are CSV files 
# files=[
    # 'img.csv',
    # 'css.csv',
    # 'file.png']
files=[
    'img.csv',
    'css.csv']

for file in files:
    if not (file.endswith('.csv')):
        print("not a csv file")
        break
else:
    print("all are csv files ")
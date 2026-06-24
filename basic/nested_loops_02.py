# select count(*) frm customers where id is NULL
# use case to navigate throug tables and column 
tables = ['customers','orders','products','prices']
columns=['id','creation_date']
for t in tables:
    for c in columns:
        print(f'select count(*) from {t} where {c} is null')
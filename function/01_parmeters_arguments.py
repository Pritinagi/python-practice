# name ="   MariA   "
# print(name.strip().lower())
case_rule="n/a" #gloabal variable

def clean_name(name):
    # print(name.strip().lower())
    print("Raw: " , name)
    cleaned=name.strip()
    if case_rule=="lower":
        cleaned = cleaned.lower()
    print("cleaned : ",cleaned)
clean_name("   AKKshItT  ")
print("The rule is : ", case_rule)
# whitespace cleanup 
text ="    engeniring".lstrip()
print(text)

text ="    engeniring     ".strip()
print(text)

text ="engeniring    ".rstrip()
print(text)


    


text ="AAAA%%%@&&#&#&#@".strip("A")
print(text)








# how to check if spacing exist without seeing the content 
# trick 
text ="engeniring    "
print(len(text))
print(len(text.strip()))
nr_of_spaces = (len(text) -len(text.strip()))
is_Clean = (len(text) ==len(text.strip())
)
print(f"no of spaces {nr_of_spaces} ")
print(f"is my data clean?? {is_Clean}" )
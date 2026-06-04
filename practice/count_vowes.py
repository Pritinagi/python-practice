# 8. Count vowels in string
word='hello'
vowels='aeiouAEIOU'
count=0
for i in word:
    if i in vowels:
        count=count+1
        print(i, "vowel exist ")
print(count)

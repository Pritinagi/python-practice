text="968-Maria, (D@t@ Engineer) ;; 27y  "

#output this  name: maria | role: data engineer | age:27

print(text.strip().strip("968-").replace('@','a').replace('(','').replace(')','').replace('y','').replace(';;',',').split(','))

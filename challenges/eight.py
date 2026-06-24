# loop through a list of days and print only the working days skipping the weekends 
days=['mon','tue','wed','thu','fri','sat','sun']
weekends= ['sat','sun']
for day in days :
    # if day =='sat' or day == 'sun':
    if day in weekends :
        continue
    else:
        print(f'its a weekday : {day}')
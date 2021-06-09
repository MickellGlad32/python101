# this programs asks the user for the number of the day of the week  and prints that said number corresponding to that day.
day = int(input('Enter the number corresponding to the day of the week (0-6).'))
if day == 0: 
    print('Sunday')
if day == 1:
    print('Monday')
if day == 2:
    print('Tuesday')
if day == 3:
    print('Wednesday')
if day == 4:
    print('Thursday')
if day == 5:
    print('Friday')
if day == 6:
    print('Saturday')
    #  if you use elif, it only checks as far as it needs to and goes no further
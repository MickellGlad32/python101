# Asks the user for a day of the week and depending on the day print either go to work or sleep in
day = int(input('What day of the week is it again? (0-6)'))

# if user inputs a range of any day during the week, tell them to go to work
if day == range(1-5):
    print('Go to work')
# else tell them to sleep in, cause its the weekend
else:
    print("It's the weekend bro, go back to sleep! ")

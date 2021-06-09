# ask for name  
user_name = input('what is your name again? ')
# greet user
print(f"Hello, {user_name}")

# check is the name is longer than 10
if len(user_name) > 10:
    # If it is say wow, that's a long name
    print("match 10")
elif len(user_name) > 5:
    print('match 5')
    # if name is not longer than 10
        # print 'thats kind of short'
        # use else in the situation where you ohly check for one condition and it handles every other condition after that
else:
    print("match everything else ")

print('Done')    
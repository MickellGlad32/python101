#  Ask for name
user_name = input('what is your name? ')
# greet user 
print(f'Hello, {user_name}')

#  check if name is longer than 10
if len(user_name) > 10:
    # if it is say 'Wow, long name'
     print('Wow, long name!')
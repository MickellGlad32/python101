# asks for inputs to find out a little bit about him/her
# name = input('What is your name ? ')
# sport_1 = input('What is the number 1 sport that you can not live without ?' )
# sport_2 = input('If you had to live without the first sport, what else would you choose ?')

# # they have to make a choice on what they like more. we just print it
# print(name + "\'s favorite sport is " + sport_1 + "." + " If " + name + " could not play that, they would play " + sport_2)

#  F-strings example
name = input('Name: ')
subject = input('Subject: ')

# story = f"{name}'s fav subject is {subject}" 

# interpolation where %s fills for your variables

story = "%s's favorite subject is %s" % (name, subject)

print(story)
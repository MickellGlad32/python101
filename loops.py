# print each time we eat a donut up to 10 times
# print('you have eaten 1 donut ')










# donuts_eaten = 1
# while donuts_eaten <= 10:
#     print (f'you have eaten {donuts_eaten} donuts.')
#     # donuts_eaten + donuts_eaten + 1
#     donuts_eaten += 1

while True:
    print('working...')
    user_input = input('Should I stop (y/n) ')
    if user_input == 'y':
        print('thank you!')
        break
    else:
        print('sight...')  

    print('finish ')             

donuts_to_eat = int(input('How many donuts are you going to eat? '))
donuts_eaten = 0
while donuts_eaten <donuts_to_eat:
    donuts_eaten += 1
    print (f'you have eaten {donuts_eaten} donuts.')
    # donuts_eaten + donuts_eaten + 1
    if (donuts_eaten == donuts_to_eat / 2):
        print('You are halfway there. ')
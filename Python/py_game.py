import random
import time

choices = {'S':'Snake','W':'Water','G':'Gun'}

x = 0
com_win = 0
user_win = 0
match_draw = 0

print('Welcome to the Snake-Water-Gun Game\n')
print('I am Mr. Computer, We will play this game 10 times')
print('Whoever wins more matches will be the winner\n')

while x < 10:
    print(f'Game No. {x+1}')
    for key, value in choices.items():
        print(f'Choose {key} for {value}')

    com_choice = random.choice(list(choices.keys())).lower()
    user_choice = input('\n----->').lower()

    if user_choice == 's' and com_choice == 'w':
        com_win += 1

    elif user_choice == 's' and com_choice == 'g':
        com_win += 1

    elif user_choice == 'w' and com_choice == 's':
        user_win += 1

    elif user_choice == 'g' and com_choice == 's':
        user_win += 1

    elif user_choice == 'g' and com_choice == 'w':
        com_win += 1

    elif user_choice == 'w' and com_choice == 'g':
        user_win += 1

    elif user_choice == com_choice:
        match_draw += 1

    else:
        print('\n\nYou entered wrong !!!!!!')
        x = 0
        print('Restarting the game')
        print('')
        time.sleep(1)
        continue

    x += 1
    print('\n')


print('Here are final stats of the 10 matches : ')
print(f'Mr. Computer won : {com_win} matches')
print(f'You won : {user_win} matches')
print(f'Matches Drawn : {match_draw}')

if com_win > user_win:
    print('\n-------Mr. Computer won-------')

elif com_win < user_win:
    print('\n-----------You won-----------')

else:
    print('\n----------Match Draw----------')

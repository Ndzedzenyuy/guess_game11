# a program that guides us and gives us a number of chances to guess the right number
from play import guess


guess()

player = input('would you love to play again?')
if player == 'yes' or 'Yes' or 'YES':
    print('run the code to play again')
else:
    print('Thanks for playing and see you next time.')












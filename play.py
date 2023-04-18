import random


def guess():
    guess_number = random.randint(1, 20)
    player_name = input('what is your name?: ')
    guess_count = 0

    while guess_count <= 3:
        guess_left = 3 - guess_count

        print(f"{player_name.upper()} Please take your time before guessing")
        if guess_left < 0:
            pass
        guess = int(input(f"{player_name.title()} enter a number between 1 amd 20 to  guess: "))
        guess_count += 1

        if guess < guess_number:
            print('number is small')
        if guess > guess_number:
            print('number is  big')
        if guess == guess_number:
            print('Congratulations, you won')
            break

        print(f'you have {guess_left} guesses left')
        print('\n')

    else:
        print(f" Ooops! The correct number is {guess_number}")







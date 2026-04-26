# Final Project
import random

print ('The NUMBER GUESSING GAME\n'
      'Your Favorite Guessing Game')
       
player= input('Player Name:')
difficulty = int(input('How many attempts do you want to give yourself(0 for unlimited):'))


def num_guess():

    rand = random.randint(1, 100)
    attempts_made = 0
    attempts_left = difficulty

    start = True


    print (f'\n Good Luck. {player}!'
           "\n I'm thinking of a number between 1 and 100")
    

    while start:
        if difficulty != 0 and attempts_left == 0:
            print(f'Game Over, you ran out of tries.\n The number was {rand}')
            start = False

        else:
            try:
                if difficulty != 0:
                    print (f'Attempts Left:{attempts_left}')
                    guess = int(input('Enter guess:'))
                    attempts_made += 1
                    attempts_left -= 1
                else:
                    guess = int(input('Enter guess:'))
                    attempts_made += 1


                if guess < rand:
                    print ('Too low! Try Again')
                elif guess > rand:
                    print('Too high! Try Again')
                else:
                    print(f'Eureka! You guessed it in {attempts_made} tries.')
                    replay = int(input('Do you want to play again?(0 for YES,1 for NO):'))

                    if replay == 0:
                        start = True

                    else:
                        start = False
            except ValueError:
                print('INVALID INPUT! Please enter a whole number')

num_guess()
import random

def mid_game_quit():
    confirm = int(input('Are you sure you want to GIVE UP? All progress will be lost(0 for YES, 1 for NO):'))
    if confirm == 0:
        return True
    return False

def handle_replay(player):
    replay = int(input('Do you want to play again?(0 for YES, 1 for NO):'))

    if replay == 0:
        user_change = int(input(f'Continue as {player}? (0 for Yes, 1 for New User):'))
        if user_change == 0:
            return True, True
        else:
            return False, True
    else:
        return False,False

print ('The NUMBER GUESSING GAME\n'
      'Your Favorite Guessing Game')

def num_guess():
    game_running = True

    while game_running:
        player = input('\nPlayer Name:')
        same_user = True

        while same_user:
            difficulty = int(input('How many attempts do you want to give yourself(0 for unlimited):'))
            rand = random.randint(1, 100)
            attempts_made = 0
            attempts_left = difficulty
            start = True

            print (f'\n Good Luck, {player}!'
                "\n I'm thinking of a number between 1 and 100")

            while start:
                if difficulty != 0 and attempts_left == 0:
                    print(f'Game Over, you ran out of tries.\n The number was {rand}')
                    
                    replay = int(input('Do you want to play again?(0 for YES, 1 for NO):'))
                    if replay == 0:
                        user_change = int(input(f'Continue as {player}? (0 for Yes, 1 for New User):'))
                        if user_change == 0:
                            start = False
                        else:
                            same_user = False
                            start = False
                    else:
                        start = False
                        same_user = False
                        game_running = False

                else:
                    try:
                        if difficulty != 0:
                            print (f'Attempts Left: {attempts_left}')
                        
                        guess = int(input('Enter guess( IF YOU WANT TO GIVE UP ENTER 999): '))

                        if guess == 999:
                            if mid_game_quit(): 
                                print(f"The number was {rand}. Better luck next time!")
                                same_user, game_running = handle_replay(player)
                                start = False
                            else:
                                print("Back to the game!")
                        elif start:
                            attempts_made += 1
                            attempts_left -= 1

                            if guess < rand:
                                print('Too low! Try Again')
                            elif guess > rand:
                                print('Too high! Try Again') 
                            else:
                                print(f'Eureka! You guessed it in {attempts_made} tries.')
                                same_user, game_running = handle_replay(player)
                                start = False
                               
                    except ValueError:
                        print('INVALID INPUT! Please enter a whole number')

num_guess()
# finalproject : Number Guessing Game


import random

def mid_game_quit():
    try:
        confirm = int(input('\nAre you sure you want to GIVE UP? (0 for YES, 1 for NO): '))
        return confirm == 0
    except ValueError:
        return False
    

def handle_replay_and_quit(player):
    try:
        replay = int(input('\nDo you want to play again? (0 for YES, 1 for NO): '))

        if replay == 0:
            user_change = int(input(f'Continue as {player}? (0 for Yes, 1 for New User): '))
            if user_change == 0:
                return True, True
            else:
                return False, True 
        else:
            return False, False 
    except ValueError:
        print("Invalid input. Ending session...")
        return False, False
    

    

print ('The NUMBER GUESSING GAME\n'
      'Your Favorite Guessing Game')

def num_guess():
    difficulty_level = {'unlimited': 0 ,'easy': 20, 'medium':10, 'hard':5, 'test':1} 
    personal_best = {}
    game_running = True

    while game_running:
        player = input('\nPlayer Name:')
        same_user = True

        while same_user:
            valid_diff = False
            
            while not valid_diff:
                print(f'AVAILABLE DIFFICULTY LEVELS {difficulty_level}')
                diff = input("Select Difficulty Level:").lower().strip()
                
                if diff in difficulty_level:
                    difficulty = difficulty_level[diff]
                    valid_diff = True
                else:
                    print(f'{diff} is not a valid level. Please check your spelling!')
                
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
                                same_user, game_running = handle_replay_and_quit(player)
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
                                if player in personal_best:
                                    if personal_best[player] > attempts_made:
                                        personal_best[player] = attempts_made
                                else:
                                     personal_best[player] = attempts_made
                                same_user, game_running = handle_replay_and_quit(player)
                                start = False
                               
                    except ValueError:
                        print('INVALID INPUT!!! Please enter a whole number')
                        
    print ('----SCORE LEADERBOARD------')
    if personal_best:
        for name in personal_best.keys():
            print(f'PLAYER: {name} || BEST SCORE: {personal_best[name]}')
    else:
        print('NO GAME WAS WON')
    print ('----THANK YOU FOR PLAYING----')

num_guess()
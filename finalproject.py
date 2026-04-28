# finalproject : Number Guessing Game


import random
def get_player_name():  #this function insures that the name input is valid using a boolean gatekeeper
    valid_name = False
    name = ""
    while not valid_name:
        name = input('\nPlayer Name: ').strip()
        if name == "":
            print("Error: Name cannot be blank.")
        elif name.isdigit():
            print("Error: Name cannot be just numbers.")
        else:
            valid_name = True
    return name

def mid_game_quit(): # this function handles a case where a user might want to quit midgame
    try:
        confirm = int(input('\nAre you sure you want to GIVE UP? (0 for YES, 1 for NO): '))
        return confirm == 0
    except ValueError:
        return False
    

def handle_replay_and_quit(player): # once a game ends, this function handles if the player wants to replay or quit the game
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
    game_running = True #boolean gatekeeper which starts with the game

    while game_running:
        player = get_player_name()
        
        same_user = True #boolean value to check if the same user is playing the game or user has changed

        while same_user:
            valid_diff = False #boolean gatekeeper to ensure a difficulty level which has been offered is chosen
            
            while not valid_diff:
                print(f'AVAILABLE DIFFICULTY LEVELS {difficulty_level}')
                diff = input("Select Difficulty Level:").lower().strip()
                
                if diff in difficulty_level:
                    difficulty = difficulty_level[diff]
                    valid_diff = True
                else:
                    print(f'{diff} is not a valid level. Please check your spelling!')
                
            rand = random.randint(1, 100)   #using random function to generate a number for the game
            attempts_made = 0
            attempts_left = difficulty
            start = True        #boolean gatekeeper to see if the game is in session(being played or not)

            print (f'\n Good Luck, {player}!'
                "\n I'm thinking of a number between 1 and 100")

            while start:
                if difficulty != 0 and attempts_left == 0: #if block to handle cases when user runs out of attempt from the difficulty chosen
                        print(f'Game Over, you ran out of tries.\n The number was {rand}')
                        same_user, game_running = handle_replay_and_quit(player)
                        start = False
                        
                else: #else block to handle the overall functioning of the game
                    try: #try and except block to ensure correct input
                        if difficulty != 0:
                            print (f'Attempts Left: {attempts_left}')
                        guess = int(input('Enter guess( IF YOU WANT TO GIVE UP ENTER 999): '))

                        if guess == 999:  #999 is the pre-set value, input 999 calls mid_game_quit if player wishes to quit
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
                                #This block runs if the user wins
                                print(f'Eureka! You guessed it in {attempts_made} tries.')
                                #Using dictionaries to store the best scores of the current session, handles both one user and multiple users.
                                if player in personal_best:
                                    if personal_best[player] > attempts_made:
                                        personal_best[player] = attempts_made
                                else:
                                     personal_best[player] = attempts_made
                                same_user, game_running = handle_replay_and_quit(player)
                                start = False
                               
                    except ValueError:
                        print('INVALID INPUT!!! Please enter a whole number')
    # the leaderboard stored in a dictionary is shown if the user quits the game, and a winning has been stored in the dictionary.                   
    print ('----SCORE LEADERBOARD------')
    if personal_best:
        for name in personal_best.keys():
            print(f'PLAYER: {name} || BEST SCORE: {personal_best[name]}')
    else:
        print('NO GAME WAS WON')
    print ('----THANK YOU FOR PLAYING----')

num_guess() #the game will start when it is called
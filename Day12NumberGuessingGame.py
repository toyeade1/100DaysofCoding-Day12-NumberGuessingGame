import random
from Day12logo import logo

def GuesstheNumber():
    guessed_number = random.randint(1,100)
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100.')
    difficulty = str(input('Choose a difficulty. Type \'easy\' or \'hard\':\n'))
    def Gameplay(lives):
        user_lives = lives
        game_end = False
        while not game_end:
            print(f'You have {user_lives} attempts remaining to guess the number.')
            user_guess = int(input('Make a guess: '))
            if user_guess == guessed_number:
                print(f'You got it! The answer was {user_guess}! ')
                game_end = True
            elif user_guess < guessed_number:
                print('Too low.')
                user_lives -= 1
            elif user_guess > guessed_number:
                print('Too high.')
                user_lives -= 1
            if user_lives > 0 and user_guess != guessed_number:
                print('Guess again.')
            if user_lives == 0:
                game_end = True
                print('You ran out of lives, Game over.')
        play_again = str(input('\nWould you like to play again? \'yes\' or \'no\'?: '))
        if play_again == 'yes':
            GuesstheNumber()
        else:
            print('Thank you for playing. Have a nice day!')
    if difficulty == 'easy':
        Gameplay(10)
    if difficulty == 'hard':
        Gameplay(5)


GuesstheNumber()

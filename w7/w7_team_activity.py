import random
game = True
back = True
while back == True:
    guesses = 0
    number = random.randint(1, 100)
    print(number)
    print('Guess My Number Game')
    print()
    while game == True:

        guess = int(input('What is your guess? '))

        if guess == number:
            print('You guessed it!') 
            guesses += 1
            print(f'It took you {guesses} guesses')
            break

        elif guess > number:
            guesses += 1
            print('Lower')
        elif guess < number:
            guesses += 1
            print('Higher')
        else:
            print('Enter a valid number')
    
    play_again = input('Do you want to play again? [yes or no] ')
    if play_again.lower() == 'no':
        exit()

if play_again.lower() == 'yes':
    back = True
import random
guesses = 0
repeat = True
back = True
index=0

name = input("What is your name? ")
print('Welcome to the word guessing game!')
while back == True:
    guesses = 0  
    print("Good Luck! ", name)
    print()

    fruits =  ['apple', 'tomato', 'melon', 
        'mango', 'lime', 'kiwi', 'grapes', 'cherry',
        'banana', 'cucumber', 'orange', 'papaya', 'pear',
        'peach']

    animals = ['panda', 'giraffe', 'bat', 'bear', 'wolf', 'zebra', 'eagle',
        'cobra', 'penguin', 'frog', 'mouse', 'rabbit', 'crow', 'whale', 'lion',
        'monkey', 'sheep', 'dogs', 'tiger']

    accessories = ['ring', 'bangle', 'lipstick', 'handbag', 'crown',
        'necklace', 'watch', 'caps', 'glasses', 'wallet',
        'belts', 'comb', 'pendent', 'earring', 'scarf',
        'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
        'jacket', 'boots', 'socks', 'stocking', 'muffler',
        'gloves', 'umbrella', 'ribbon']

    stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
        'files', 'fevicol', 'inkpot', 'chalk', 'duster',
        'glue', 'paper', 'cutter', 'chart', 'colours',
        'stapler', 'marker', 'staples', 'clips', 'calculator',
        'envelope', 'register']

    countries = ['afghanistan', 'australia', 'austria', 'belize', 'bolivia',
        'liberia', 'brazil', 'guatemala', 'haiti', 'india', 'israel',
        'japan', 'italy', 'mexico', 'mongolia']

    words = fruits + animals + accessories + stationary + countries
    secret_word = random.choice(words)

    while repeat == True:
        if secret_word in fruits:
                print("Pay attention:\nYour word is a Fruit")
        elif secret_word in accessories:
                print("Pay attention:\nYour word is related to Accessory")
        elif secret_word in stationary:
                print("Pay attention:\nYour word is related to Stationary")
        elif secret_word in animals:
                print("Pay attention:\nYour word is an Animal")
        elif secret_word in countries:
                print("Pay attention:\nYour word is a Contry")

        print(f'and has {len(secret_word)} letters')
        print(secret_word)
    
        print('Your hint is:')
        for char in secret_word:
            print('_', end =' ')
        print(' ')
        guess_word = input('What is your guess? ')
        guess_word = guess_word.lower()

        
        for char in guess_word:
            if len(guess_word) != len(secret_word):
                print('_', end=' ')
            elif char in secret_word:
                if guess_word[index] == secret_word[index]:
                    print(char.upper(), end= ' ')
                else:
                    print(char.lower(), end=' ')
            else:
                print('_', end=' ')
            index+=1
        print()
        index=0

        if len(guess_word) != len(secret_word):
            print('Sorry, the guess must have the same number of letters as the secret word.')
            guesses += 1
          
        elif guess_word != secret_word:
                print("""That's not the word!\nKeep looking!""")
                print()
                guesses += 1
                repeat = True
        else:
            if secret_word == guess_word:    
                print(f'Congratulations {name}, You guessed it!')
                guesses += 1
                break

    print("The word is: ", secret_word)
    print(f'It took you {guesses} guesses') 
    print()

    play_again = input('Do you want to play again? [yes or no] ')
    if play_again.lower() == 'no':
        exit()
    print()
if play_again.lower() == 'yes':
    back = True
elif secret_word == guess_word:
                print(char.upper(), end=' ')
            
            elif secret_word != guess_word:
                print(char.lower(), end=' ')




 for char in secret_word:
            if len(guess_word) != len(secret_word):
                print('_', end=' ')
           # elif char in guess_word:
                #print(char.upper(), end=' ')
            #else:
                #print('_', end=' ')
            #print()



---------------------------------


char_word = ""
        for x in range(len(secret_word)):
            #print(f'La letra en el lugar {x} es igual?')
            #print(secret_word[x] == guess_word[x])

            if secret_word[x] == guess_word[x]:
                char_word = char_word + secret_word[x].upper()
            elif secret_word[x] in guess_word:
                char_word = char_word + guess_word[x].lower()
            else:
                char_word != char_word + '_'
        
        print(char_word)



 #print(f'La letra en el lugar {x} es igual?')
            #print(secret_word[x] == guess_word[x])
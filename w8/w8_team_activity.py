print('Iterating Through Strings')
print()

back = 'yes'

nelson_quote= 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'

while back == 'yes':
    back = back.lower()
    ask_number = int(input('Please enter a whole number: '))

    for position, letter in enumerate(nelson_quote, start=0):
        if position % ask_number == 0:
            print(letter.upper(), end='')
        else:
            print(letter.lower(), end='')
    print()

    back = input('Do you want to enter another number? [YES or NO]: ')

    if back == 'no':
        exit('Thanks for your reply')
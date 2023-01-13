print('Integer Comparator')

first_number = (input('What is the first number? '))
second_number = (input('What is the second number? '))
print()

if first_number.isdigit():
        print('First number entered correctly')
    
else:
        print('Error: The first element entered is not a whole number')
        exit('Try again')

if second_number.isdigit():
            print('Second number entered correctly')
else:
        print('Error: The second element entered is not a whole number')
        exit('Try again')
print()
if first_number == second_number:
        print('The numbers are equal')
elif first_number != second_number:
        print('The numbers are not equal')
if first_number > second_number:
        print('The first number is greater')
elif second_number > first_number:
        print('The second number is greater')
if first_number < second_number:
        print('The first number is not greater')
elif second_number < first_number:
        print('The second number is not greater')

print()
animal = input('What is your favorite animal? ')
if animal.lower() == 'bear':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite')

"""
What is the first number? 4
What is the second number? 3
The first number is greater
The numbers are not equal
The second number is not greater

What is your favorite animal? giraffe
That one is not my favorite.
"""
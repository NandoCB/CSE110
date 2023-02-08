ride_authorization = False

print('Amusement Park Rides')
print()

print ('---------- First Rider Information ----------')
age1 = int(input('What is the age of the first rider? '))
height1 = int(input('What is the height of the first rider? '))
print ()

second_rider = input('Is there a second rider (yes/no)?')
print()

if second_rider == 'yes':
    print ('---------- Second Rider Information ----------')
    age2 = int(input('What is the age of the first rider? '))
    height2 = int(input('What is the height of the first rider? '))
    print ()
    print('Evaluating the entered information of the players')

    # first basic rule

    #Rule 1
    if height1 < 36 or height2 < 36:
        ride_authorization = False

    else: 
            if age1 >= 18 or age2 >= 18:
                ride_authorization = True
            else:
                ride_authorization = False
else:  #Rule 2
    if age1 >= 18 and height1 >= 62:
        ride_authorization = True
    else:
        ride_authorization = False

if ride_authorization:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print ('Sorry, you may not ride.')

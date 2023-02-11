ride_authorization = False

print('Amusement Park Rides')
print()

print ('---------- First Rider Information ----------')
age1 = int(input('What is the age of the first rider? '))
height1 = int(input('What is the height of the first rider? '))
print ()
                            #STRETCH CHALLENGE #1a
if age1 >= 12 and age1 < 18:
    golden_passport1 = input('The runner has a Golden Passport? [yes or no] ')
    golden_passport1 = golden_passport1.lower()
second_rider = input('Is there a second rider (yes/no)? ')
print()

if second_rider == 'yes':
    print ('---------- Second Rider Information ----------')
    age2 = int(input('What is the age of the first rider? '))
    height2 = int(input('What is the height of the first rider? '))
    print ()                    #STRETCH CHALLENGE #1b
    if age2 >= 12 and age2 < 18:
        golden_passport2 = input('The runner has a Golden Passport? [yes or no] ')
        golden_passport2 = golden_passport2.lower()
        
    print('Evaluating the entered information of the players')

    
#######################################################################################
    #Rule 1
    if height1 < 36 or height2 < 36:
        ride_authorization = False

    else:                                       #STRETCH CHALLENGE #2
            if age1 >= 18 or age2 >= 18 or golden_passport1 == 'yes' or golden_passport2 == 'yes':
                ride_authorization = True
            
            else:
########################################################################################
                                                #STRETCH CHALLENGE #3
                if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
                    ride_authorization = True
                elif (age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16):
                    ride_authorization = True
                else:
                    ride_authorization = False
######################################################################################## 

else:  #Rule 2
        if age1 >= 18 and height1 >= 62:
            ride_authorization = True
        else:
            ride_authorization = False

if ride_authorization:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print ('Sorry, you may not ride.')

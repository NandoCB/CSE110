import math
v = 0
star_again = True
while star_again == True:

    t_unit_measurement = input('Fahrenheit or Celsius (F/C)?: ')
    t_unit_measurement = t_unit_measurement.lower()

    if t_unit_measurement == 'f':
        t = float(input('What is the air temperature? '))
        for v in range(5, 61, 5):
            wci = 35.74 + (0.6221 * t) - (35.75 * pow(v,0.16)) + (0.4275 * t * pow(v,0.16))
            print(f'At temperature {t}F, and wind speed {v} mph, the windchill is {round(wci, 2)}F')
        print()
            
        finish = input('Do you wish to continue? (Y/N): ')
        print()
        finish = finish.lower()
        if finish == 'y':
            print('Please enter the unit of measure.')
            star_again = True
        else:
            star_again = False


    elif t_unit_measurement == 'c':
        celsius = float(input('Enter the temperature in degrees celsius: '))
        for v in range(5, 61, 5):
            fahrenheit = (celsius * 9/5) + 32
            wci = 35.74 + (0.6215 * fahrenheit) - (35.75 * pow(v,0.16)) + (0.4275 * fahrenheit * pow(v,0.16))
            print(f'At temperature {round(fahrenheit, 2)}F, and wind speed {v} mph, the windchill is {round(wci, 2)}F')
        print()
            
        finish = input('Do you wish to continue? (Y/N): ')
        print()
        finish = finish.lower()
        if finish == 'y':
            print('Please enter the unit of measure.')
            star_again = True
        else:
            star_again = False
    else:
        print('Enter a valid character (F/C)')
        print()
        star_again = True
import math

print('''Speed of a Falling Object\nWelcome to the velocity calculator. Please enter the following:''')
print()

print('Enter the data to calculate the c value')

p = float(input('p = Density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water): '))
a = float(input('A = Cross sectional area of projectile (in square meters): '))
drag_c = float(input('C = Drag constant (0.5 for sphere, 1.1 for cylinder): '))

c = (1 / 2) * p * a * drag_c
print('------------------------------------------------')
print()
print(f'The inner value of c is: {round(c, 3)}')
print('------------------------------------------------')


print('Enter the data to calculate the speed of a falling object')

t = float(input('time (in seconds): '))
m = float(input('mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))

v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) *t))

print('------------------------------------------------')
print()
print(f'The velocity after {t} seconds is: {round(v, 3)} m/s')
print('------------------------------------------------')

"""
v(t) = math.sqrt(mg/c) * (1 - math.exp((-math.sqrt(mgc)/m)t))

 
"""

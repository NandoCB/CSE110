import math 
print('Areas of Shapes')

square_length = float(input('What is the length of a side of the square? '))
square_area = (math.pow(square_length, 2))
print(f'The area of the square is: {round(square_area, 2)}')


rectangle_length = float(input('What is the length of rectangle? '))
rectangle_width = float(input('What is the width of the rectangle? '))
rectangle_area = (rectangle_width * square_length)
print(f'The area of the rectangle is: {rectangle_area}')

circle_radius = float(input('What is the radius of the circle? '))
area_circle = (math.pow(circle_radius, 2) * math.pi)
print(f'The area of the circle is: {round(area_circle,2)} ')


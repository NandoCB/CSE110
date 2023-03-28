import math

#Area Square #########################################################################
def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area
#Area_Rectangle ######################################################################
def compute_area_rectangle(length, width):
    return length * width
#Area Circle #########################################################################
def compute_area_circle(radius):
    return math.pi * radius * radius
######################################################################################

def compute_area(shape, value1, value2=0):
    area = -1

    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)
    
    return area

shape = ""

while shape != "quit":
    shape = input("What shape do you have? ")

    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area(shape, side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area(shape, length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area(shape, radius)
        print(f"The area is {area}")
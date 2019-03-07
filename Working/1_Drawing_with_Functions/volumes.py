'''
----------------------------------------------------
Name:     volumes.py
Purpose:  To calculate the volume of a cylinder,
          cone, or sphere based on user input

Author:   Terry.Kim
Created:  07/03/19
----------------------------------------------------
'''

# Imports the math library
import math

# Defines the function that calculates the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * (radius**2) * height

# Defines the function that calculates the volume of a cone
def cone_volume(radius, height):
    return math.pi * (radius**2) * (height/3)

# Defines the function that calculates the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * (radius**3)

# Main function that runs the other functions
def main():
    radius = float(input('Enter a radius: '))
    height = float(input('Enter a height: '))
    print('')

    print(round(cylinder_volume(radius, height), 2))
    print(round(cone_volume(radius, height), 2))
    print(round(sphere_volume(radius), 2))

# Running the main function
main()

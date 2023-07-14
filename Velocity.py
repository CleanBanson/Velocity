


'''
m = mass (in kg)

g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)

t = time (in seconds)

c = 1/2 p A C

p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)

A = cross sectional area of projectile (in square meters)

C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)

exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).

'''





'''
Author: Matthew Harris
Start Date: May 1, 2022
File: Velocity.py
'''

import math




answer = input('Would you like to calculate the velocity of an object in time? Y/N ')

if answer.upper() == 'Y':
    print('Ok, enter the following data: \n')
else: 
    quit()


mass = float(input('What is the mass of the object in kg? '))
gravity = float(input('What is the acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)'))
time = float(input('What is the time (in seconds)? '))
density = float(input('What is the density of the fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)? '))
area = float(input('What is the cross sectional area of projectile (in square meters)? '))
drag = float(input("What is the drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. "))



print()
print()
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

c = (1 / 2) * density * area * drag
velocity = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))
v_terminal = math.sqrt(mass * gravity / c)
print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after {time:.1f} seconds is: {velocity:.3f} m/s')
print(f'The terminal velocity would be: {v_terminal:.3f}')






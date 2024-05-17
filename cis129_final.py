# Final
# Author: Branden Quach
# May 16, 2024

print(f'Answer for Question 1')
total = 12.8 + 18.2 + 0.4
print(total)

print(f'Answer for Question 2')
number = float(input(f'Enter a float number: '))
print(f'{number} is a float.')

print(f'Answer for Question 3')
pi = 3.14159
r = 3.5
d = 2 * r
c = 2 * r * pi
a = pi * (r ** 2)
print(f'For a circle with a radius of {r}, the diameter is {d}, circumference is {c}, and area is {a}.')

print(f'Answer for Question 4')
print('number  square  cube')
for number in range(0, 6):
    print('{0:3d}\t {1:3d}\t {2:3d}'.format(number, number * number, number * number * number))

print(f'Answer for Question 5')
y = 0
z = 0
x = int(input(f'Enter an integer'))
if x > 100:
    y = 20
    z = 40
print(f'y is {y} and z is {z}')

print(f'Answer for Question 6')
list = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
average = sum(list)/len(list)
print(f'The class average is {average}.')

print(f'Answer for Question 7')
for numbers in range(33, -1, -3):
    print(numbers, end=' ')

print(f'\nAnswer for Question 8')
myInt = 0
def squared(myInt):
    myInt = int(input(f'Enter an integer to be squared.'))
    myInt = myInt ** 2
    return myInt
squaredNumber =squared(myInt)
print(squaredNumber)

print(f'Answer for Question 9')
from random import randint
rolls = 10
rollcount = 0
for amount in range(0, rolls):
    rollcount += 1
    print(f'Roll {rollcount}:',randint(1,6))

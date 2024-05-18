# Final
# Author: Branden Quach
# May 17, 2024

print(f'\nAnswer for Question 1:')
total = 12.8 + 18.2 + 0.4
print(total)

print(f'\nAnswer for Question 2:')
number = float(input(f'Enter a float number: '))
print(f'{number} is a float.')

print(f'\nAnswer for Question 3:')
pi = 3.14159
r = 3.5
d = 2 * r
c = 2 * r * pi
a = pi * (r ** 2)
print(f'For a circle with a radius of {r}, the diameter is {d}, circumference is {c}, and area is {a}.')

print(f'\nAnswer for Question 4:')
print('number  square  cube')
for number in range(0, 6):
    print('{0:3d}\t {1:3d}\t {2:3d}'.format(number, number * number, number * number * number))

print(f'\nAnswer for Question 5:')
y = 0
z = 0
x = int(input(f'Enter an integer'))
if x > 100:
    y = 20
    z = 40
print(f'y is {y} and z is {z}')

print(f'\nAnswer for Question 6:')
list = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
average = sum(list)/len(list)
print(f'The class average is {average}.')

print(f'\nAnswer for Question 7:')
for numbers in range(33, -1, -3):
    print(numbers, end=' ')

print(f'\n\nAnswer for Question 8:')
myInt = 0
def squared(myInt):
    myInt = int(input(f'Enter an integer to be squared.'))
    myInt = myInt ** 2
    return myInt
squaredNumber =squared(myInt)
print(squaredNumber)

print(f'\nAnswer for Question 9:')
from random import randint
rolls = 10
rollcount = 0
for amount in range(0, rolls):
    rollcount += 1
    print(f'Roll {rollcount}:',randint(1,6))

print(f'\nAnswer for Question 10:')
list1 = [10,20,30]
list2 = [40,50]
concatenated_list = list1 + list2
print(concatenated_list)

print(f'\nAnswer for Question 11:')
x = 'ABC'
x = '#'.join(x)
print(x)

print(f'\nAnswer for Question 12:')
country_codes = {'Finland':'fi','South Africa':'za','Nepal':'np'}
for key in country_codes.keys():
    print(key)

print(f'\nAnswer for Question 13:')
x = chr(66)
print(f'{x}')

print(f'\nAnswer for Question 14:')
with open('accounts.txt', 'w') as file:
    file.write('100 Bill 12.34\n200 Joe 0.00\n300 Tom 4.21')

with open('accounts.txt', 'r') as file:
    print(file.read())

print(f'\nAnswer for Extra Credit:')
def main():
    Car = myCar(0, 0, '')
    Car.set_year(2020)
    Car.set_cylinders(4)
    Car.set_start_engine('Start your engine')
    print(f'Year:', Car.get_year())
    print(f'Cylinders:', Car.get_cylinders())
    print(Car.get_start_engine())

class myCar():
    def __init__(self, year, cylinders, start_engine):
        self.year = year
        self.cylinders = cylinders
        self.start_engine = start_engine
    def myCar(self, y, c, s):
        myCar.year = y
        myCar.cylinders = c
        myCar.start_engine= s
    def set_year(self, y):
        self.year = y
    def set_cylinders(self, c):
        self.cylinders = c
    def set_start_engine(self, s):
        self.start_engine = s
    def get_year(self):
        return self.year
    def get_cylinders(self):
        return self.cylinders
    def get_start_engine(self):
        return self.start_engine
main()

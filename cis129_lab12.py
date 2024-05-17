# Lab 12: Pet Class
# Author: Branden Quach
# May 16, 2024
# Prints input into a check protected format

# Main function
def main():
    # Variables
    inputName = ''
    inputType = ''
    inputAge = 0
    # Class variable
    Animal = Pet('', '', 0)
    # Prompts pet name
    inputName = input(f'Enter a pet name: ')
    Animal.setName(inputName)
    # Prompts pet type
    inputType = input(f'Enter a pet type: ')
    Animal.setType(inputType)
    # Prompts pet age
    inputAge = int(input(f'Enter a pet age: '))
    Animal.setAge(inputAge)
    # Prints values entered
    print(f'The pet name is', Animal.getName())
    print(f'The pet type is', Animal.getType())
    print(f'The pet age is', Animal.getAge())

# Pet class
class Pet():
    # Private
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
    # Constructor
    def Pet(self, n, t, a):
        Pet.name = n
        Pet.type = t
        Pet.age = a
    # Mutators
    def setName(self, n):
        self.name = n
      
    def setType(self, t):
        self.type = t
      
    def setAge(self, a):
        self.age = a
    
    def getName(self):
        return self.name
      
    def getType(self):
        return self.type
      
    def getAge(self):
        return self.age
# Calls main function
main()

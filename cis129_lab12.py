# Lab 12: Pet Class
# Author: Branden Quach
# May 16, 2024
# Prints input into a check protected format

def main():
    inputName = ''
    inputType = ''
    inputAge = 0
  
    Animal = Pet('', '', 0)
  
    inputName = input(f'Enter a pet name: ')
    Animal.setName(inputName)
  
    inputType = input(f'Enter a pet type: ')
    Animal.setType(inputType)
  
    inputAge = int(input(f'Enter a pet age: '))
    Animal.setAge(inputAge)

    print(f'The pet name is ', Animal.getName())
    print(f'The pet type is ', Animal.getType())
    print(f'The pet age is ', Animal.getAge())
  
class Pet:
    def __init__(self, n, t, a):
        self.name = n
        self.type = t
        self.age = a
      
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
      
main()

# This property allows a class to inherit attributes and methods from another class it allows for reusability of code and extensibility

class Animal:
    def __init__(self,name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")  

# after the class pass the class to inherit in brackets as shown below
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass

dog = Dog('scooby')
cat=Cat('ifif')
mouse=Mouse('kiki')

print(dog.name)
mouse.eat()


class Car:
    def __init__(self,name,transmission,engineSize):
        self.name= name
        self.transmission=transmission
        self.engineSize=engineSize

        def driving(self):
            print(f"This{self.name} of transmission{self.transmission} and engine size of {self.engineSize}cc")

        # def braking(self)    

class Toyota(Car):
    def __init__(self,yom,color):
        self.yom=yom
        self.color=color
        self.isFourWheel=True

    def fourWheel(self):
        if self.isFourWheel==True:
            print(f"The {self.name} is a fourwheel drive ")     

class Mazda(Car):
    def __init__(self,yom,color):
        self.yom=yom
        self.color=color
        self.isFourWheel=False

    def fourWheel(self):
        if self.isFourWheel==False:
            print(f"The {self.name} is not a fourwheel drive ")  

car1=Car('Toyota','manual',2000)
car2=Mazda(2000,'black')
car3=Toyota(2024,'gray')
print(car1.name)
print(f"My {car1.name} with a transmission of{car1.transmission} is a {car3.isFourWheel} ")

                  
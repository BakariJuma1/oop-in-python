# inheriting from more than one class 
class Prey:
    def flee(self):
        print('this animal flees')
class Predator:
    def hunt(self):
        print('this animal hunts')
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabit = Rabbit()
fish = Fish()
fish.hunt()
print(rabit.flee())



# my example 
class School:
    def __init__(self,name):
        self.name=name
    def mySchool(self):
        print(f"i study at {self.name}")    
class Student(School):
    pass
class Grade(Student):
    pass        
class wellBeing(Student):
    pass

school=School('lga')
school.mySchool()
print(school.name)
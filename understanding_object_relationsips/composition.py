import sys
sys.path.append("/home/bakari/development/code/phase-3/Python 101/OOP/")
from understanding_object_relationsips.class_engine import Engine
from understanding_object_relationsips.class_wheel import Wheel

class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.make=make
        self.model=model
        # composition 
        self.engine=Engine(horse_power)
        self.wheels=[Wheel(wheel_size)for wheel in range(4)]

    def display_car(self):
        return f"{self.make}{self.model}  {self.engine.horse_power}(hp) {self.wheels[0].size}inches"    

carOne =Car(make='ford',model='mustang',horse_power=500,wheel_size=18)
print(carOne.display_car())
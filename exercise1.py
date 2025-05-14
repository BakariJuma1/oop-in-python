
class Circle:
      pi =3.14

      def __init__(self,radius):
            self.radius=radius

      def circumfrence(self):
            return 2*Circle.pi*self.radius 
      def area(self):
            return 2*Circle.pi*self.radius


circleOne=Circle(4)
# print(circleOne.circumfrence()) 
circleTwo=Circle(10) 
# print(circleTwo.area())   


class Rectangle:
      
      def __init__(self,length,width):
            self.length=length
            self.width=width
      def findArea(self):
            return self.length*self.width
      

rectangleOne=Rectangle(4,5)
print(f" Area of a rectangle is {rectangleOne.findArea()}")     

class SimpleInterest:
      def __init__(self,principle,rate,time):
            self.principle=principle
            self.rate = rate
            self.time=time

      def calcSimpleInterest(self):
            return ( (self.principle*self.rate*self.time)/100)
      

client=SimpleInterest(10000,5,2)
print(f"Your simple intrest is {client.calcSimpleInterest()}")      




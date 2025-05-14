
class Circle:
      pi =3.14

      def __init__(self,radius):
            self.radius=radius

      def circumfrence(self):
            return 2*Circle.pi*self.radius 
      def area(self):
            return 2*Circle.pi*self.radius


circleOne=Circle(4)
print(circleOne.circumfrence()) 
circleTwo=Circle(10) 
print(circleTwo.area())   



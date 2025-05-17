class User:
    def logIn(self):
        self.loggedIn=True

class Student(User):

    def logIn(self):
         super().logIn()  
         self.inClass=True      

studentOne=Student()
print(studentOne.logIn())         
# defined outside constructor
# shared among all instances of a class 


class Student:

    # This are class variable shared
    class_year=2024
    numStudents=0

    def __init__(self,name,age):
        # instance variable
        self.name=name
        self.age=age
        Student.numStudents += 1

student1=Student('ken',30)
student2=Student('joy',30)
student3=Student('line',40)
student4=Student('bingo',50)

print(student1.class_year)
print(student2.name)
# accessing the class variable
print(Student.numStudents)

print(f"my graduating class of {Student.class_year} has {Student.numStudents} students")
class Student:
    school_name=''
    student_count=0

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        Student.student_count+=1
     
    def get_info(self):
        return(f"{self.name} Grade:{self.grade}") 
    
    @classmethod
    def number_of_student(cls):
        return(f"total student{cls.student_count}")
     
    @classmethod
    def change_school_name(cls,new_name):
        cls.school_name=new_name
        return cls.school_name
    
student_one=Student('bakari',60)
student_two=Student('joe',30)
student_three=Student('ken',40)
student_four=Student('ian',90)

Student.change_school_name('Moringa')
print(f'i am {student_one.get_info()} and this is my school {Student.school_name} ')   
print(f'{Student.school_name} school has a total of {Student.number_of_student()}')

 
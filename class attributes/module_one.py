class Student:
    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count +=1
        Student.total_gpa+=1


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name}{self.gpa}"    
    
    @classmethod
    def get_count(cls):
        return f"total of students {cls.count}"
    @classmethod
    def get_total_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return(f"average gpa:{cls.total_gpa/cls.count}")
    
studentOne=Student('juma',35)
student_two=Student('kk',78)    

print(f'{Student.get_count()} with a gpa of {Student.get_total_gpa()}')
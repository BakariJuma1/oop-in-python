myCourses=['chem','math','English']

def showCourse(myCourses):
    for course in myCourses:
        #  print('This are my courses')
         return(course)

def arts(myCourses):
    for artCourse in myCourses:
        if artCourse=='English':
            return(artCourse)
        
def apply_to_each(fn,myCourses):
    print('applying to each ')
    print(f"Here are your semester courses  {fn(myCourses)}")

apply_to_each(arts,myCourses)    
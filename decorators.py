def makeSoup():
    return('soup')

# decorator to add salt to soup
def addSalt(func):
    def wrapper():
        return func() +'with salt'
    return wrapper

@addSalt
def makeSoup():
    return 'soup'

print(makeSoup())


def callStudent():
    return('student')

def tallStudent(func):
    def wrapper():
        return(func()+"6ft tall")
    return wrapper

@tallStudent
def callStudent():
    return('student')


print(f"THe student called is {callStudent()}")    
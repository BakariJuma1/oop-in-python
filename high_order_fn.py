# function as a high order function
# function passed as an argument
def greetLouder(name):
    print(f'hello am{name.upper()}')

def greetSofter(name):
    print(f"hello am {name.lower()}")    

def display(fn,name):
    print('displaying the function ')   
    fn(name)

display(greetLouder,'JUMA')
display(greetSofter,'ken')

# returning a function
def jobValidation(name,age):
    print('validating applicants')
    def names():
        print(f'my name is{name}')
    def printAge():
        print(f'you are {age} old under the required age')

    if age >= 18:
        print("welcome proceed with your  applications ")
        return names
    else:
        print(f"hey{name} you can not apply")  
        return printAge

job=jobValidation('bakari',20)
job()
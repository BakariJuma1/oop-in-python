def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def divide(x,y):
    return x/y

def rem(x,y):
    return x%y


def calculate(fn,x,y):
    print('displaying calculate')
    print(f"your solution is {fn(x,y)}")


calculate(mul,4,5)

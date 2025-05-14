class Human:
    def eat(self):
        print('i can eat ')

    def work(self):
        print('i can walk')    


class Male(Human):
   
    def flirt(self):
        print('i can flirt')

    def work(self):
        super().work()
        print('i can code ')      
class Female(Human):
    pass

bakari=Male()
print(bakari.work())
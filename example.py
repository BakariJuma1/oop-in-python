class Bot:
    # class variable

    def __init__(self,name):
        self.name=name
        self.health=name
        self.damage=0
        self.armour=100

    def fire(self):
        print('firing my first shot')    
assaultBot=Bot(name='kk',)        
print(assaultBot.name)

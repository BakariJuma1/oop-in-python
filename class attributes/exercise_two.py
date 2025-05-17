class Pet:
    total_pets=0
    

    def __init__(self,name,species):
        self.name=name
        self.species=species
        Pet.total_pets+= 1

    def describe(self):
        return(f"{self.name} is a {self.species}")
    
    @classmethod
    def from_string(cls,pet_string):
        name,species =pet_string.split(',')
        return cls(name.strip(),species.strip())
    
    @classmethod
    def get_total_pets(cls):
        return(f"total pets:{cls.total_pets}")

petOne=Pet('max','dog')
petTwo=Pet.from_string('whiskers,cat')
print(petTwo.describe())
print(Pet.get_total_pets())

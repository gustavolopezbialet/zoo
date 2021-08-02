from animal import Animal

class Bear(Animal):
    def __init__(self, name, age, habitat, heath_level, hapiness_level, bear_type):
        super().__init__(name, age, habitat, heath_level, hapiness_level)
        self.bear_type = bear_type
        

"""leon = Bear('simba', 5,'sabana', 50, 30)
print (leon.heath_level)
print (leon.hapiness_level)
leon.eating()
print (leon.heath_level)
print (leon.hapiness_level)
"""
        
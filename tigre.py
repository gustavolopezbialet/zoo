from animal import Animal

class Tiger(Animal):
    def __init__(self, name, age, habitat, heath_level, hapiness_level):
        super().__init__(name, age, habitat, heath_level, hapiness_level)

    def eating(self, eat):
        if eat < 7:
            self.heath_level += 8
            self.hapiness_level += 10
        elif eat <= 20:
            self.heath_level += 15
            self.hapiness_level += 20
        else:
            self.heath_level += 22
            self.hapiness_level += 28
        return self

"""leon = Tiger('simba', 5,'sabana', 50, 30)
print (leon.heath_level)
print (leon.hapiness_level)
leon.eating(10)
print (leon.heath_level)
print (leon.hapiness_level)
"""
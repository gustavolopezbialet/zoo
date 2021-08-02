# from animal import Animal
from leon import Lion
from tigre import Tiger
from oso import Bear

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal.name == new_animal.name:
                return False
        self.animals.append(new_animal)
        return True

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal.display_info())


"""new_animal = Lion('simba', 5,'sabana', 50, 30, False)

 
zoo1.add_animal(new_animal)
"""
"""zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
"""
# zoo1.print_all_info()

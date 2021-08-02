class Animal():
    def __init__(self, name, age, habitat, heath_level = 0, hapiness_level = 0):
        self.name = name
        self.age = age
        self.heath_level = heath_level
        self.hapiness_level = hapiness_level
        self.habitat = habitat

    def display_info(self):
        return f'Hola me llamo {self.name}, nivel de salud {self.heath_level} manzanas y nivel de felicidad {self.hapiness_level} corazones, vivo en {self.habitat} '
    
    def eating(self):
        self.heath_level += 10
        self.hapiness_level += 10
        return self
            
            

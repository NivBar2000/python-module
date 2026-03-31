class animals:
    def __init__(self, name, type, age, food):
        self.name = name
        self.type = type
        self.age = age
        self.food = food
  


class dog(animals):
    def __init__(self, name, type, age, food, barking_volum):
        super().__init__(name, type, age, food)
        self.barking_volum = barking_volum
      

class Mouse(animals):
    def __init__(self,name, type, age, food, size, damge):
        super().__init__(name, type, age, food)
        self.size = size
        self.damge = damge
        
class bird(animals):
    def __init__(self, name, type, age, food, is_flying, flying_speed):
        super().__init__(name, type, age, food,)
        self.is_flying=True
        self.flying_speed = flying_speed
        
    def fly(self):
            self.is_flying = True
            pass
        
    def not_fly(self):
            self.is_flying=False
            pass

class fish(animals):
    def __init__(self,name, type, age, food, swimming_speed):
        super().__init__(name, type, age, food)
        self.swimming_speed = swimming_speed
    

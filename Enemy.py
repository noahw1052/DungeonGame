import random as r
class Enemy:
    def __init__(self,name,health,min_attack,max_attack):
        self.name = name
        self.original_health = health
        self.health = health
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.awake = "Awake"
    def attack(self):

        x = r.randint(self.min_attack,self.max_attack)
        y = r.randint(1,20)

        if y == 10:
            x = 20

        else:
            x = x
        return x
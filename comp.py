from random import randint

class Comp:
    def __init__(self):
        self.score = 0

    def pick(self):
        return randint(1,3)
    
    def increase_point(self):
        self.score += 1
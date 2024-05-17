class User:
    def __init__(self):
        self.score = 0
    
    def get_user_input(self):
        user_pick = int(input("Pick one: Scissor(1), Rock(2), Paper(3)\n"))
        while user_pick < 1 or user_pick > 3:
            user_pick = int(input("Pick one: Scissor(1), Rock(2), Paper(3)\n"))
        return user_pick
    
    def increase_point(self):
        self.score += 1
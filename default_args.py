#Default arguments

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y = self.y + change

    def move_down(self, change=5):
        self.y = self.y - change

    def move_right(self, change=2):
        self.x = self.x + change

    def move_left(self, change=2):
        self.x = self.x - change


player1 = Player(5, 10)
player1.move_up()
print(player1.y)
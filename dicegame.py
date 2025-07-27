#ejemplo completo de Aggregation

import random

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value
    

class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    

    def increment_counter(self):
        self._counter = self._counter + 1

    def decrement_counter(self):
        self._counter = self._counter - 1

    def roll_die(self):
        return self.die.roll()
    
my_die = Die()
player1 = Player(my_die, is_computer=True)
print(player1.roll_die())


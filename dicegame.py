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
        self._counter = 10 # --porque este atributo no esta como un parametro?: Porque este es el valor por defecto. No es necesario pasarlo como un argumento cada vez que se crea un objeto, porque la clase ya sabe que valor usar si no se le dice lo contrario. Esto es muy util cuando un atributo siempre debe empezar con el mismo valor.

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
    

class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    
    def play(self):
        print('Welcome to the dice game')
        print('-----------------------')

        while True:
            self.play_round()
            game_over = self.check_game_over()

            if game_over == True:
                break

    
    def play_round(self):
        #welcome the user
        self.print_round_welcome()

        #roll de dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #show the values
        self.show_dice(player_value, computer_value)

        #check winner and loser
        if player_value > computer_value:
            print('You won the round')
            self.update_counters(winner=self._player, loser=self._computer)

        elif computer_value > player_value:
            print('The computer won the round')
            self.update_counters(winner=self._computer, loser=self._player)

        else:
            print('Its a draw')
            
        #show counters
        self.show_counters()


    def print_round_welcome(self):
        print('--- New Round ---')
        input(' Press any key to roll the dice.')

    def show_dice(self, player_value, computer_value):
        print(f'Your die: {player_value}')
        print(f'Computer die: {computer_value}')

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f'Your counter: {self._player.counter}')
        print(f'Computer counter: {self._computer.counter}')
    
    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print('Computer Won')
        else:
            print('You won the game')



#Create Instances
player_die = Die()
cpu_die = Die()

player1 = Player(player_die, is_computer=False)
cpu = Player(cpu_die, is_computer=True)

game = DiceGame(player1, cpu)

#start the game
game.play()
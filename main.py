import random
import sys



#User Properties
class Player:
    def __init__(self):
        print('Welcome to RPS 2500 !')


        self.score = 0
        self.username=input('Your Name?: ')
        self.moves: dict = {'rock': '🪨', 'paper':'📰', 'scissors':'✂️'}
        self.valid_moves: list[str]= list(self.moves.keys())

    def choice(self):
        while True:

            player_input = input('Rock, Paper, Scissors>> ').lower()
            if player_input == 'exit':
                print('Thank you for Playing the Game')
                sys.exit()
            if player_input not in self.valid_moves:
                print ('Invalid Move...')
                return self.choice()
            else:
                return player_input
            
class Computer: 
    def __init__(self):
        self.score = 0
        self.name ='AI'
        self.moves: dict = {'rock': '🪨', 'paper':'📰', 'scissors':'✂️'}
        self.valid_moves: list[str]= list(self.moves.keys())
    

    def choice(self):
        ai_move = random.choice(self.valid_moves)
        print(ai_move)
        return ai_move


class Game:
    def __init__(self):
        self.max_round = 3
        self.round = 0
        self.player = Player()
        self.computer = Computer()


    def play(self):
        while self.round < self.max_round:
            player_move = self.player.choice()
            computer_move = self.computer.choice()
            self.adjust_scores(player_move,computer_move)
            self.display_scores()
        winner = self.determine_winner()
        print(f'{winner} Won!')

    def adjust_scores(self,player_move,computer_move):
        if player_move == computer_move:
            print('it is a tie Continue')
            return
        if((computer_move =='rock' and player_move == 'scissors') or
            (computer_move == 'paper' and player_move=='rock')or
            (computer_move == 'scissors' and player_move == 'paper')):
            print('AI won the Round')
            self.computer.score +=1
        else:
            print(f'{self.player.username} won the Round')
            self.player.score +=1
        self.round +=1

    def determine_winner(self):
        return self.computer.name if self.computer.score > self.player.score else self.player.username

    def display_scores(self):
        print('-----------------')
        print(f'{self.player.username} score:{self.player.score}')
        print(f'{self.computer.name} score:{self.computer.score}')

if __name__ == "__main__":
    game = Game()
    game.play()
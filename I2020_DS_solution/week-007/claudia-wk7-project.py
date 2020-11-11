import random
class RockPaperScissor:
    def __init__(self, rounds=3):
        self.rounds = rounds
        self.score = {
            'computer': 0,
            'player': 0
        }
    
    def computers_turn(self):
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors'
        }
        turn = random.randint(0,2)
        return (turn, choices[turn])
    
    def my_turn(self):
        turn = int(input("Enter 0 for rock, 1 for paper, 2 for scissors "))
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors'
        }
        return (turn, choices[turn])
        
    def compare_turns(self, computer, player):        
        if computer == player:
            print('Tied')
            return self.run()
        elif computer == 'rock' and player == 'scissors':
            self.score['computer'] += 1
            return "Computer Wins"
        elif computer == 'scissors' and player == 'paper':
            self.score['computer'] += 1
            return "Computer Wins"
        elif computer == 'paper'and player == 'rock':
            self.score['computer'] += 1
            return "Computer Wins"
        elif computer == 'scissors'and player == 'rock':
            self.score['player'] += 1
            return "Player Wins"
        elif computer == 'rock'and player == 'paper':
            self.score['player'] += 1
            return "Player Wins"
        elif computer == 'paper' and player == 'scissors':
            self.score['player'] += 1
            return "Player Wins"
    
    def run(self):
        while self.rounds > 0:
            my_turn = self.my_turn()
            computers_turn = self.computers_turn()        
            print(self.compare_turns(computers_turn[1], my_turn[1]))
            self.rounds -= 1
        return self.score
    
if __name__ == '__main__':
    rps = RockPaperScissor()
    rps.run()
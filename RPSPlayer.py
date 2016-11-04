import random

class RPSPlayer():
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        
        
    def player_turn(self):
        choice = input("Choose (R)ock, (P)aper, or (S)cissors ").upper()
        if choice == "R":
            self.choice = 0
        elif choice == "P":
            self.choice = 1
        elif choice == "S":
            self.choice = 2
        return int(self.choice)

    def comp_turn(self):
        self.choice = random.randint(0, 2)
        return int(self.choice)

    def win(self):
        self.wins += 1
        
    def lose(self):
        self.losses += 1

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_choice(self):
        return int(self.choice)

    
    def toString(self):
        print("Name:", self.name, "Wins:", self.get_wins(), "Losses:", self.get_losses())
    
        
        

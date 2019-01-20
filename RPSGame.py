import random
import sys


class RPSGame:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.choices = {'R': 0, 'P': 1, 'S': 2}

    @property
    def games(self) -> int:
        return self.wins + self.losses + self.ties

    @property
    def win_rate(self) -> int:
        return self.wins / self.games if self.games > 0 else 0

    @property
    def win_percentage(self) -> int:
        return self.win_rate * 100

    @property
    def loss_rate(self) -> int:
        return self.losses / self.games if self.games > 0 else 0

    @property
    def loss_percentage(self) -> int:
        return self.loss_rate * 100

    @property
    def tie_rate(self) -> int:
        return self.ties / self.games if self.games > 0 else 0

    @property
    def tie_percentage(self) -> int:
        return self.tie_rate * 100

    def player_turn(self):
        choice = None
        while choice is None:
            player_input = input(
                "Choose (R)ock, (P)aper, or (S)cissors ").upper()
            choice = self.choices.get(player_input)
            if choice is None:
                print("Enter a valid choice")
        return int(choice)

    def comp_turn(self):
        choice = random.randint(0, 2)
        return int(choice)

    def win(self):
        self.wins += 1
        print("you won!")
        print(self)

    def lose(self):
        self.losses += 1
        print("you lost")
        print(self)

    def tie(self):
        self.ties += 1
        print("you tied")
        print(self)

    def evaluate_choices(self, choice1, choice2):
        """Returns 0 in a tie 1 for win -1 for lose."""
        if choice1 == choice2:
            return 0
        if choice1 == 0 and choice2 == 2 or choice1 == 1 and choice2 == 0 or choice1 == 2 and choice2 == 1:
            return 1
        return -1

    def play(self, cli_args):
        try:
            play_again = True
            while play_again:
                player_choice = self.player_turn() if not cli_args.computer else self.comp_turn()
                comp_choice = self.comp_turn()
                result = self.evaluate_choices(player_choice, comp_choice)
                if result == 0:
                    self.tie()
                elif result == -1:
                    self.lose()
                elif result == 1:
                    self.win()
                if self.games > cli_args.rounds - 1:
                    play_again = False
        except KeyboardInterrupt:
            pass
        finally:
            print(self.long_str)

    @property
    def long_str(self):
        def format_percentage(p): return '{0:.3g}'.format(p)
        return f"Games played: {self.games}, Win percentage: {format_percentage(self.win_percentage)}, Loss percentage: {format_percentage(self.loss_percentage)}, Tie percentage: {format_percentage(self.tie_percentage)}, {self}"

    def __str__(self):
        return f"Wins: {self.wins}, Losses: {self.losses}, Ties: {self.ties}"

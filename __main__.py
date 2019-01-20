from RPSGame import RPSGame
from args import parser

if __name__ == '__main__':
    args = parser.parse_args()
    game = RPSGame()
    game.play(args)

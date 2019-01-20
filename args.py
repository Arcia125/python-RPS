import argparse
import math

parser = argparse.ArgumentParser(
    description='Play rock paper scissors via CLI')
parser.add_argument(
    '--rounds', default=math.inf, help='Maximum rounds to play', type=int, required=False
)
parser.add_argument(
    '--computer', help='Computer vs computer', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)

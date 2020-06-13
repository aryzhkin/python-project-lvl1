from brain_games.games import brain_calc
from brain_games.common import game_engine


def main():
    game_engine.play_game(brain_calc)


if __name__ == '__main__':
    main()
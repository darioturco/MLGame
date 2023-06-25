from src.games.four_in_line import FourInLine
from src.algorithms.q_learning import QLearning

def player_human(game):
    game.render()
    x = int(input("\nX: "))

    return (x, )

def four_in_line_test():
    fil = FourInLine(render_mode = 'human', height=4, width=4)
    fil.render()

    algorithm = QLearning(fil, learning_rate=0.98, discount_factor=0.25, explore_rate=0.1)
    hystory = algorithm.fit(epochs=10000)

    print(hystory['reward'])

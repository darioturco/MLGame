#import tests.test_tic_tac_toe
from src.games.tic_tac_toe import TicTacToe
from src.algorithms.q_learning import QLearning

def player_human(game):
    game.print_board()
    x = int(input("\nX: "))
    y = int(input("\nY: "))

    return (x, y)

def tic_tac_toe_test():
    ttt = TicTacToe(render_mode = 'human')
    ttt.render()

    algorithm = QLearning(ttt, 0.95, 0.25, 0.1)
    hystory = algorithm.fit(epochs=1000000)

    print(hystory['reward'])

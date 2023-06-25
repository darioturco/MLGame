import gymnasium as gym
import numpy as np
import time
from src.algorithms.q_learning import QLearning

def frozen_lake_test():

    # create the environment
    env = gym.make("FrozenLake-v1", render_mode='ansi', is_slippery=False)

    env.reset()
    env.render()    # Show the ambient

    algorithm = QLearning(env, 0.95, 0.25, 0.1)
    hystory = algorithm.fit(epochs=10000)

    print(hystory['reward'])

    # close the environment
    env.close()

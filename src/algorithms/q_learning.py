import random
import numpy as np
from src.utils import *

class QLearning(object):
    def __init__(self, env, learning_rate, discount_factor, explore_rate):
        self._Q = np.zeros((env.observation_space.n, env.action_space.n))
        self._env = env
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self._explore_rate = explore_rate
        self._state_dict = {}
        self._action_dict = {}
        self._state_count = 0
        self._action_count = 0
        self._iterable_action = hasattr(env.action_space.sample(), '__iter__')

    def fit(self, epochs=1000):
        print('Starting training...')
        history = {'reward': []}

        for i in range(epochs):
            state, _ = self._env.reset()
            state = self.state_to_index(state)

            done = False
            total_reward = 0
            while not done:
                print(f'Epoach: {i}')
                action = self.predict(state)
                next_state, reward, done, truncated, info = self._env.step(action)
                action = self.action_to_index(action)
                next_state = self.state_to_index(next_state)
                self.q_learning(state, action, next_state, reward)
                state = next_state
                total_reward += reward

            history['reward'].append(total_reward)

        return history

    def q_learning(self, state, action, next_state, reward):
        self._Q[state, action] += self._learning_rate * \
                                    (reward + self._discount_factor * np.max(self._Q[next_state]) - self._Q[state, action])

    def predict(self, state):
        if np.max(self._Q[state]) > 0:
            action_index = np.argmax(self._Q[state])
            action = self.index_to_action(action_index)
        else:
            action = self._env.action_space.sample()
        return action

    ### Only works when the state is a list of lists or an integer
    def state_to_index(self, state):
        if hasattr(state, '__iter__'):
            tuple_state = tuple(tuple(r) for r in state)
            if tuple_state not in self._state_dict:
                self._state_dict[tuple_state] = self._state_count
                self._state_count += 1

        else:
            return state

        return self._state_dict[tuple_state]

    def action_to_index(self, action):
        if self._iterable_action:
            tuple_action = tuple(action)
            if tuple_action not in self._action_dict:
                self._action_dict[tuple_action] = self._action_count
                self._action_count += 1

        else:
            return action

        return self._action_dict[tuple_action]

    def index_to_action(self, index):
        if self._iterable_action:
            for action in self._action_dict:
                if self._action_dict[action] == index:
                    return action
        else:
            return index

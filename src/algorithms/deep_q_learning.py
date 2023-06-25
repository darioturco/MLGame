import random
import tensorflow as tf
import numpy as np
from collections import deque

class DeepQLearning(object):
    def __init__(self, env, gamma, epsilon, warm_up, model):
        self._env = env
        self._gamma = gamma
        self._epsilon = epsilon
        self._warm_up = warm_up

        self._state_dimension = env.observation_space.shape
        self._action_dimension = env.action_space.n

        #print(f'{self._state_dimension=}')
        #print(f'{self._action_dimension=}')

        self._replay_buffer_size = 10000
        self._batch_replay_buffer_size = 1000
        self._update_target_network_period = 15

        self._counter_update_target_network = 0

        self._sum_rewards_for_episode = []
        self._replay_buffer = deque(maxlen=self._replay_buffer_size)

        #self._online_network = self.create_network() # main network
        #self._target_network = self.create_network()
        self._online_network = model
        self._target_network = tf.keras.models.clone_model(model)

        self._target_network.set_weights(self._online_network.get_weights())

        self._actions_append = []

    def loss_function(self, y_true, y_pred):
        s1,s2 = y_true.shape

        indices = np.zeros(shape=(s1, s2))
        indices[:,0] = np.arange(s1)
        indices[:,1] = self._actions_append

        # gather_nd and mean_squared_error are TensorFlow functions
        loss = tf.keras.losses.mean_squared_error(tf.gather_nd(y_true, indices=indices.astype(int)), tf.gather_nd(y_pred, indices=indices.astype(int)))
        return loss

    def start_warm_up(self):
        temp_buffer = []
        actions = 0
        for index_episode in range(self._warm_up):

            rewards = []
            episode_history = []
            done = False
            state, _ = self._env.reset()
            while not done:
                action = env.action_space.sample()
                next_state, reward, done, truncated, info = self._env.step(action)

                rewards.append(reward)
                episode_history.append((state, action, reward, next_state, done))
                state = next_state
                actions += 1

            temp_buffer.append((episode_history.copy(), np.sum(rewards)))

        temp_buffer.sort(key = lambda x : x[1])
        for i in range(min(self._replay_buffer_size, actions)):
            for t in temp_buffer[-i][0]:
                self._replay_buffer.append(t)

        self.train_network()

    def training_episodes(self, number_episodes):
        if self._warm_up is not None:
            self.start_warm_up()

        for index_episode in range(number_episodes):
            state, info = self._env.reset()
            rewards = []
            done = False

            i = 0
            while not (done or (i > 1000)):
                action = self.select_action(state, index_episode)
                next_state, reward, done, truncated, info = self._env.step(action)

                rewards.append(reward)
                self._replay_buffer.append((state, action, reward, next_state, done))
                state = next_state
                i = i + 1

            self.train_network()

            sum_reward = np.sum(rewards)
            self._sum_rewards_for_episode.append(sum_reward)
            print(f'Sum of rewards of episode {index_episode} is: {sum_reward}', flush=True)

    # Reveer es muy fea esta funcion
    def select_action(self, state, index):
        if (np.random.random() < self._epsilon):
            if index > 200:
                self._epsilon = 0.99 * self._epsilon

            return self._env.action_space.sample()

        else:
            #print(state)
            #print(state.shape)

            Qvalues = self._online_network.predict(state.reshape((1,) + self._state_dimension), verbose=None)
            return np.random.choice(np.where(Qvalues[0,:] == np.max(Qvalues[0,:]))[0])

    def train_network(self):

        # if the replay buffer has at least batchReplayBufferSize elements,
        # then train the model
        # otherwise wait until the size of the elements exceeds batchReplayBufferSize
        if (len(self._replay_buffer) > self._batch_replay_buffer_size):

            # sample a batch from the replay buffer
            randomSampleBatch = random.sample(self._replay_buffer, self._batch_replay_buffer_size)

            # here we form current state batch
            # and next state batch
            # they are used as inputs for prediction
            currentStateBatch = np.zeros(shape=((self._batch_replay_buffer_size,) + self._state_dimension))
            nextStateBatch = np.zeros(shape=((self._batch_replay_buffer_size,) + self._state_dimension))

            # this will enumerate the tuple entries of the randomSampleBatch
            # index will loop through the number of tuples
            for index, tupleS in enumerate(randomSampleBatch):
                # first entry of the tuple is the current state
                currentStateBatch[index] = tupleS[0]
                # fourth entry of the tuple is the next state
                nextStateBatch[index] = tupleS[3]

            # here, use the target network to predict Q-values
            QnextStateTargetNetwork = self._target_network.predict(nextStateBatch)
            # here, use the main network to predict Q-values
            QcurrentStateMainNetwork = self._online_network.predict(currentStateBatch, verbose=None)

            # now, we form batches for training
            # input for training
            inputNetwork = currentStateBatch
            # output for training
            outputNetwork = np.zeros(shape=(self._batch_replay_buffer_size, self._action_dimension))

            # this list will contain the actions that are selected from the batch
            # this list is used in my_loss_fn to define the loss-function
            self._actions_append = []
            for index, (currentState, action, reward, nextState, terminated) in enumerate(randomSampleBatch):

                # if the next state is the terminal state
                if terminated:
                    y = reward
                # if the next state if not the terminal state
                else:
                    y = reward + self._gamma * np.max(QnextStateTargetNetwork[index])

                # this is necessary for defining the cost function
                self._actions_append.append(action)

                # this actually does not matter since we do not use all the entries in the cost function
                outputNetwork[index] = QcurrentStateMainNetwork[index]
                # this is what matters
                outputNetwork[index, action] = y


            # here, we train the network
            self._online_network.fit(inputNetwork, outputNetwork, batch_size = self._batch_replay_buffer_size, verbose=None, epochs=80)

            self._counter_update_target_network += 1
            if(self._counter_update_target_network > (self._update_target_network_period-1)):
                self._target_network.set_weights(self._online_network.get_weights())
                self._counter_update_target_network = 0
                print("Target network updated!")

    def save(self, path='partial_trained_online.h5'):
        self._online_network.save(path)

    def load(self, path='partial_trained_online.h5', args=None):
        self._online_network = tf.keras.models.load_model(path, custom_objects=args)
        self._target_network = tf.keras.models.clone_model(self._online_network)

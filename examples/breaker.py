import sys
import signal
import gymnasium as gym
import tensorflow as tf
from src.algorithms.deep_q_learning import DeepQLearning

def breaker_test():
    #def signal_keyboard_interrupt_handler(signal, frame):
    #    print("You pressed Ctrl+C, saving and exit...")
    #    sys.exit(0)
    #signal.signal(signal.SIGINT, signal_keyboard_interrupt_handler)

    def create_network():
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Input(shape=(210, 160, 3)))
        model.add(tf.keras.layers.Conv2D(32, 8, strides=4, activation="relu"))
        model.add(tf.keras.layers.Conv2D(64, 4, strides=2, activation="relu"))
        model.add(tf.keras.layers.Conv2D(64, 3, strides=1, activation="relu"))
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(512, activation='relu'))
        model.add(tf.keras.layers.Dense(4, activation='linear'))
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001, clipnorm=1.0), loss=tf.keras.losses.Huber(), metrics=['accuracy'])
        return model

    env = gym.make("ALE/Breakout-v5", render_mode=None)
    env.metadata['render_fps'] = 20
    state, _ = env.reset()

    dqn = DeepQLearning(env, gamma=0.99, epsilon=0.1, warm_up=None, model=create_network())
    dqn.training_episodes(3)
    dqn._online_network.save("trained_model_temp.h5")

    model = tf.keras.models.load_model("trained_model_temp.h5", custom_objects={'loss_function': DeepQLearning.loss_function})
    env = gym.make("ALE/Breakout-v5", render_mode='human')
    staste, _ = env.reset()

    done = False
    sum_reward = 0

    while not done:
        action = env.action_space.sample()
        next_state, reward, done, truncated, info = env.step(action)

        env.render()
        sum_reward += reward
        state = next_state

    print(f'Total Reward = {sum_reward}')
    env.close()

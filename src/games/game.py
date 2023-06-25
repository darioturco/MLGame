import numpy as np

class Game(object):

    def __init__(self):
        print("Initiating Game...")


import numpy as np

class Discrete(object):
    def __init__(self, n, seed=None, start=0):
        self.n = n
        self._start = start
        self._seed = seed

    def sample(self):
        return int(np.random.random() * self.n) + self._start

    def __repr__(self):
        return str({i + self.start for i in range(self.n)})

class MultiDiscrete(object):
    def __init__(self, nvec, seed=None):
        self.nvec = np.array(nvec)
        self.n = np.prod(self.nvec)
        self._seed = seed

    def sample(self):
        return (np.random.random(self.nvec.shape) * self.nvec).astype(np.int64)

    def __repr__(self):
        return str(self.nvec)

import numpy as np


class Problem:
    def __init__(self, dim, min_val, max_val, is_min_prob: bool = False):
        self.dim = dim
        self.min_val = min_val
        self.max_val = max_val
        self.is_min_prob = is_min_prob

    def solution_fitness(self, solution):
        pass

    def init_range(self):
        pass


class FunctionOptimization(Problem):

    def __init__(self, dim, min_val, max_val, is_min_prob: bool = False):
        super().__init__(dim, min_val, max_val, is_min_prob)

    def solution_fitness(self, solution):
        return 5000 - 10 * solution[0] + 40 * solution[1] + solution[0] * solution[1] \
               - 0.8 * (solution[1] ** 2) - 0.5 * (solution[0] ** 2)

    def init_range(self):
        return np.random.uniform(0, 100, self.dim)



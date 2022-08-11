import random

import numpy as np


class Function:
    def __init__(self, dim: int, type: bool):
        self.dim = dim
        self.type = type

    def solution_fitness(self, x, y):
        return 5000 - 10 * x + 40 * y + x * y - 0.8 * (y ** 2) - 0.5 * (x ** 2)


class Problem:
    def __init__(self, dim, min_val, max_val):
        self.dim = dim
        self.min_val = min_val
        self.max_val = max_val

    def solution_fitness(self, solution):
        pass

    def init_range(self):
        pass


class Func1(Problem):

    def __init__(self, dim, min_val, max_val):
        super().__init__(dim, min_val, max_val)

    def solution_fitness(self, solution):
        return 5000 - 10 * solution[0] + 40 * solution[1] + solution[0] * solution[1] \
               - 0.8 * (solution[1] ** 2) - 0.5 * (solution[0] ** 2)

    def init_range(self):
        return np.random.uniform(0, 100, self.dim)

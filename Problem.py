class Function:
    def __init__(self, dim: int, type: bool):
        self.dim = dim
        self.type = type

    def fitness(self, x, y):
        return 5000 - 10 * x + 40 * y + x * y - 0.8 * (y ** 2) - 0.5 * (x ** 2)

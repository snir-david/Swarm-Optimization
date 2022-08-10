class Particle:
    def __init__(self):
        self.local_best = 0
        self.global_best = 0
        self.fitness = 0
        self.position = None
        self.velocity = 0




class Swarm:
    def __init__(self, size):
        self.swarm_size = size
        self.swarm = []
        self.best_fitness = 0

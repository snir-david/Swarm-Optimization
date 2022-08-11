import numpy as np


class Particle:

    def __init__(self, w, c1, c2, swarm):
        self.fitness = 0
        self.local_best_fitness = 0
        self.local_best_position = self.position = np.random.uniform(0, 100, 2)
        self.velocity = 0
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.swarm = swarm


class Swarm:
    def __init__(self, size, w, c1, c2, fitness, prob_dim, is_min_prob=True, need_init: bool = True):
        self.swarm_size = size
        self.swarm = []
        self.global_best_fitness = 0
        self.global_best_position = None
        self.global_best_particle = None
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.is_min_prob = is_min_prob
        self.fitness = fitness
        self.dim = prob_dim
        if need_init:
            self.init_swarm()

    def init_swarm(self):
        for i in range(self.swarm_size):
            p = Particle(self.w, self.c1, self.c2, self)
            p.fitness = self.fitness(p.position[0], p.position[1])
            self.swarm.append(p)
            if p.fitness > self.global_best_fitness:
                self.set_global_best(p)

    def new_velocity(self, p: Particle):
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)
        v_t_1 = self.w * p.velocity + self.c1 * r1 * (p.local_best_position - p.position) \
                + self.c2 * r2 * (self.global_best_position - p.position)
        p.velocity = v_t_1

    def new_position(self, p: Particle):
        self.new_velocity(p)
        x_t_1 = p.position + p.velocity
        p.position = x_t_1
        p.fitness = self.fitness(p.position[0], p.position[1])
        if p.fitness > self.global_best_fitness:
            self.global_best_fitness = p.fitness
            self.global_best_position = p.position
        if p.fitness > p.local_best_fitness:
            p.local_best_fitness = p.fitness
            p.local_best_position = p.position

    def local_best_update(self, p: Particle):
        if self.is_min_prob:
            pass

    def set_global_best(self, p: Particle):
        self.global_best_fitness = p.fitness
        self.global_best_position = p.position
        self.global_best_particle = p


import numpy as np


class Particle:

    def __init__(self, swarm, init_func):
        self.fitness = 0
        self.local_best_fitness = 0
        self.local_best_position = self.position = init_func()
        self.velocity = 0
        self.swarm = swarm


class Swarm:
    def __init__(self, size, w, c1, c2, problem, need_init: bool = True):
        self.swarm_size = size
        self.swarm = []
        # global best
        self.global_best_fitness = 0
        self.global_best_position = None
        self.global_best_particle = None
        # Hyper-Parameters
        self.w = w
        self.c1 = c1
        self.c2 = c2
        # Problem
        self.problem = problem
        if need_init:
            self.init_swarm()

    def init_swarm(self):
        for i in range(self.swarm_size):
            # initialize particle
            p = Particle(self, self.problem.init_range)
            # calc fitness
            p.fitness = self.problem.solution_fitness(p.position)
            self.swarm.append(p)
            # compare current particle fitness with global best
            if self.compare_fitness(p.fitness, self.global_best_fitness):
                self.set_global_best(p)

    def new_velocity(self, p: Particle):
        # random variables
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)
        # calc new velocity using the equation - v(t+1)= w * v(t) + c1 * r1 * (local_best - x(t))
        # + c2 * r2 * (global_best - x(t))
        v_t_1 = self.w * p.velocity + self.c1 * r1 * (p.local_best_position - p.position) \
                + self.c2 * r2 * (self.global_best_position - p.position)
        p.velocity = v_t_1

    def new_position(self, p: Particle):
        # calc new velocity
        self.new_velocity(p)
        # calc new position
        x_t_1 = p.position + p.velocity
        p.position = x_t_1
        # calc new fitness and check it against the local and global
        p.fitness = self.problem.solution_fitness(p.position)
        if self.compare_fitness(p.fitness, self.global_best_fitness):
            self.set_global_best(p)
        if self.compare_fitness(p.fitness, p.local_best_fitness):
            p.local_best_fitness = p.fitness
            p.local_best_position = p.position

    def compare_fitness(self, f1: int, f2: int):
        # check if the problem is min or max and compare accordingly
        # min problem
        if self.problem.is_min_prob:
            if f1 < f2:
                return True
            return False
        else:  # max problem
            if f1 > f2:
                return True
            return False

    def set_global_best(self, p: Particle):
        self.global_best_fitness = p.fitness
        self.global_best_position = p.position
        self.global_best_particle = p

import Problem
from Swarm import *
from Problem import *

SWARM_SIZE = 10
W = 0.1
C1 = 0.1
C2 = 0.8


def find_best_sol(swarm: Swarm):
    while True:
        for particle in swarm.swarm:
            swarm.new_position(particle)
        print(f'Best Particle in position {swarm.global_best_position} and the fitness is {swarm.global_best_fitness}')


if __name__ == '__main__':
    prob = Function(2, True)
    swarm = Swarm(SWARM_SIZE, W, C1, C2, prob.fitness, prob.dim)
    find_best_sol(swarm)

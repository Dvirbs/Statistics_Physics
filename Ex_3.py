# Dvir Ben Simchon and Noa Goldberg
# Ex 3 - Statistics
import math

import numpy as np


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int((int(n * multiplier) / multiplier) * 10)


class Particle:
    """
    class that describe the particle data
    """

    def __init__(self, name: str, location: list, velocity: list):
        """
        A constructor for a Particle object
        :param name: A string representing the particle's name
        :param location:  tuple representing the particle's (x, y) location
        :param velocity: tuple representing the particle's (v_x, v_y) velocity
        """
        self.radius = 0.15
        self.name = name
        self.location = location
        self.velocity = velocity
        self.dt_wall = [0, 0]
        self.update_dt_wall()

    def update_dt_wall(self):
        """

        :return:
        """
        for i in range(2):
            if self.velocity[i] > 0:
                self.dt_wall[i] = abs((1 - self.location[i] - self.radius) / self.velocity[i])
            elif self.velocity[i] < 0:
                self.dt_wall[i] = abs((self.location[i] - self.radius) / self.velocity[i])


class Board:
    """
    class that represent the board
    """

    def __init__(self):
        """

        """
        self.particles = []
        self.position_particle_counter = np.zeros((10, 10, 4))
        self.vx_particle_counter = np.zeros((200, 4))  # -V_max until +V_max
        self.vy_particle_counter = np.zeros((200, 4))  # -V_max until +V_max
        self.vabs_particle_counter = np.zeros((100, 4))  # 0 until +V_max

        self.mat_board = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    def update_dt_wall_all(self):
        """

        :return:
        """
        for particle in self.particles:
            particle.update_dt_wall()

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        board = list()
        for row in range(10):
            board.append(list())
            for column in range(10):
                board[row].append('_')

        for particle in self.particles:
            board[round_down(particle.location[0], 1)][round_down(particle.location[1], 1)] = str(particle.name)

        current_stat_str = ''
        for row_i, row in enumerate(board):
            if row_i > 0:
                current_stat_str += '\n'
            for col in row:
                current_stat_str += col
        return current_stat_str


def first_particle_and_min_time(part1, part2, part3, part4) -> list[float, Particle, int]:
    list_dt_wall = np.array([part1.dt_wall[0], part1.dt_wall[1], part2.dt_wall[0], part2.dt_wall[1], part3.dt_wall[0],
                    part3.dt_wall[1], part4.dt_wall[0], part4.dt_wall[1]])
    i = np.argmin(list_dt_wall)
    dt_first = list_dt_wall[i]
    first_part = i // 2     # + 1  (interested in index which starts from 0)
    if i % 2 == 0:
        p_axis = 0
    else:
        p_axis = 1
    return [dt_first, first_part, p_axis]


if __name__ == '__main__':
    print_every = 10000
    p1 = Particle("p1", [0.25, 0.25], [0.21, 0.12])
    p2 = Particle("p2", [0.25, 0.75], [0.78, 0.34583])
    p3 = Particle("p3", [0.75, 0.25], [-0.23, -0.79])
    p4 = Particle("p4", [0.75, 0.75], [0.71, 0.18])
    t = 0
    counter = 0
    particle_wall_coll_counters = np.array([0, 0, 0, 0])
    box = Board()
    box.particles = [p1, p2, p3, p4]
    while counter <= 10**7:
        box.update_dt_wall_all()
        dt_coll = (0, 0)
        # TODO calculate dt_coll
        dt, first_p, axis = first_particle_and_min_time(p1, p2, p3, p4)
        for p in box.particles:
            p.location[0], p.location[1] = p.location[0] + dt * p.velocity[0], p.location[1] + dt * p.velocity[1]
        # TODO change location of particles in board
        box.particles[first_p].velocity[axis] *= -1
        counter += 1
        particle_wall_coll_counters[first_p] += 1
        t += dt
        print("************************************")
        print(box)
        print("************************************")

        if counter % print_every == 0:
            if np.sum(particle_wall_coll_counters) % print_every != 0:
                raise Exception('not updating particle wall collisions properly')
            print(particle_wall_coll_counters)




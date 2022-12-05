# Dvir Ben Simchon and Noa Goldberg
# Ex 3 - Statistics
import math

import numpy as np
import matplotlib.pyplot as plt


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int((int(n * multiplier) / multiplier) * 10)


def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])


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

    def update_self_velocity(self, e_x, e_y, s_v):
        self.velocity[0] += e_x*s_v
        self.velocity[1] += e_y*s_v


class Board:
    """
    class that represent the board
    """

    def __init__(self):
        """

        """
        self.particles = []
        self.mat_board = np.zeros((10, 10, 4))
        # self.vx_particle_counter = np.zeros((200, 4))  # -V_max until +V_max
        # self.vy_particle_counter = np.zeros((200, 4))  # -V_max until +V_max
        # self.vabs_particle_counter = np.zeros((100, 4))  # 0 until +V_max
        # particle_1
        self.vx_particle1_counter = []  # -V_max until +V_max
        self.vy_particle1_counter = []  # -V_max until +V_max
        self.vabs_particle1_counter = []  # 0 until +V_max
        # particle_2
        self.vx_particle2_counter = []  # -V_max until +V_max
        self.vy_particle2_counter = []  # -V_max until +V_max
        self.vabs_particle2_counter = []  # 0 until +V_max
        # particle_3
        self.vx_particle3_counter = []  # -V_max until +V_max
        self.vy_particle3_counter = []  # -V_max until +V_max
        self.vabs_particle3_counter = []  # 0 until +V_max
        # particle_4
        self.vx_particle4_counter = []  # -V_max until +V_max
        self.vy_particle4_counter = []  # -V_max until +V_max
        self.vabs_particle4_counter = []  # 0 until +V_max

        # self.mat_board = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        #                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    def update_positions(self, dt_diff):
        """

        :param dt_diff: the dt between t to dt_store / the time witch we need to move the particle for storing
        :return:
        """
        for index, particle in enumerate(self.particles):
            self.mat_board[9 - round_down((particle.location[1] + dt_diff * particle.velocity[1]),
                                          1)][round_down(particle.location[0] + dt_diff * particle.velocity[0], 1)][index] += 1

    def update_velocity(self):
        particle_1 = self.particles[0]
        self.vx_particle1_counter.append(particle_1.velocity[0])
        self.vy_particle1_counter.append(particle_1.velocity[1])
        v_tot = sum([particle_1.velocity[0]**2+particle_1.velocity[1]**2])**0.5
        self.vabs_particle1_counter.append(v_tot)
        particle_2 = self.particles[1]
        self.vx_particle2_counter.append(particle_2.velocity[0])
        self.vy_particle2_counter.append(particle_2.velocity[1])
        v_tot = sum([particle_2.velocity[0]**2+particle_2.velocity[1]**2])**0.5
        self.vabs_particle2_counter.append(v_tot)
        particle_3 = self.particles[2]
        self.vx_particle3_counter.append(particle_3.velocity[0])
        self.vy_particle3_counter.append(particle_3.velocity[1])
        v_tot = sum([particle_3.velocity[0]**2+particle_3.velocity[1]**2])**0.5
        self.vabs_particle3_counter.append(v_tot)
        particle_4 = self.particles[3]
        self.vx_particle4_counter.append(particle_4.velocity[0])
        self.vy_particle4_counter.append(particle_4.velocity[1])
        v_tot = sum([particle_4.velocity[0]**2+particle_4.velocity[1]**2])**0.5
        self.vabs_particle4_counter.append(v_tot)


    def update_velocity_both(self, argument_list, col_particles):
        """
        :param col_particles: are index of particles that collide
        :return:
        """
        e_x, e_y, s_v = argument_list[0], argument_list[1], argument_list[2]
        i = col_particles[0]
        j = col_particles[1]
        self.particles[i].update_self_velocity(e_x, e_y, s_v)
        self.particles[j].update_self_velocity(-e_x, -e_y, s_v)

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
                board[row].append(' _ ')

        for particle in self.particles:
            board[9 - round_down(particle.location[1], 1)][round_down(particle.location[0], 1)] = " " + str(particle.name) + " "
            board[9 - round_down(particle.location[1], 1)][round_down(particle.location[0], 1) + 1] = ' * '
            board[9 - round_down(particle.location[1], 1)][round_down(particle.location[0], 1) - 1] = ' * '
            board[9 + 1 - round_down(particle.location[1], 1)][round_down(particle.location[0], 1)] = ' * '
            board[9 - 1 - round_down(particle.location[1], 1)][round_down(particle.location[0], 1)] = ' * '

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


def coll_time(p_list: [Particle]):
    min_col_time = 10**5
    flag = 0
    for i, p_i in enumerate(p_list):
        for j, p_j in enumerate(p_list):
            if j <= i:
                continue
            d_x, d_y = p_j.location[0] - p_i.location[0], p_j.location[1] - p_i.location[1]
            d_l_2 = d_x ** 2 + d_y**2
            d_l = d_l_2 ** 0.5
            d_vx, d_vy = p_j.velocity[0] - p_i.velocity[0], p_j.velocity[1] - p_i.velocity[1]
            d_v_2 = d_vx ** 2 + d_vy ** 2
            s = d_vx * d_x + d_vy * d_y
            gamma = s**2 - d_v_2 * (d_l_2-4*p_i.radius**2)

            if gamma > 0 and s < 0:
                flag = 1
                coll_t_ij = -(s+gamma**0.5)/d_v_2
                if coll_t_ij < min_col_time:
                    collisions_particles = [i, j]
                    e_x = d_x / d_l
                    e_y = d_y / d_l
                    s_v = d_vx * e_x + d_vy * e_y
                min_col_time = min(min_col_time, coll_t_ij)
            else:
                coll_t_ij = 10**4
                min_col_time = min(min_col_time, coll_t_ij)
    if flag:
        return min_col_time, collisions_particles, [e_x, e_y, s_v]
    else:
        return min_col_time, "No Collisions", "empty list"


if __name__ == '__main__':
    print_every = 10000
    p1 = Particle("p1", [0.25, 0.25], [0.21, 0.12])
    p2 = Particle("p2", [0.25, 0.75], [0.71, 0.18])
    p3 = Particle("p3", [0.75, 0.25], [-0.23, -0.79])
    p4 = Particle("p4", [0.75, 0.75], [0.78, 0.34583])
    t = 0
    dt_store = 1
    counter = 0
    particle_wall_counters = np.array([0, 0, 0, 0])
    particle_coll_counters = np.array([0, 0, 0, 0])
    box = Board()
    box.particles = [p1, p2, p3, p4]
    box.update_positions(0)
    while counter <= 10**7:    #10**7
        box.update_dt_wall_all()
        dt_coll_min, firsts_p_ij_col, arg_list = coll_time(box.particles)   # firsts_p_ij_col is indexes i and j
        dt_wall_min, first_p, axis = first_particle_and_min_time(p1, p2, p3, p4)
        wall_or_coll = 0 if dt_wall_min < dt_coll_min else 1
        dt = min(dt_wall_min, dt_coll_min)
        if 0 < ((t + dt) // dt_store - t):
            # update store position
            diff_t = round(((t + dt) // dt_store - t)*100)/100
            box.update_positions(diff_t)
            # update store velocity
            box.update_velocity()

        # updates Position in The particle world by dt_min(coll/wall)
        for p in box.particles:
            p.location[0], p.location[1] = p.location[0] + dt * p.velocity[0], p.location[1] + dt * p.velocity[1]

        # updates Velocity
        if wall_or_coll == 0:
            box.particles[first_p].velocity[axis] *= -1
            particle_wall_counters[first_p] += 1
        else:
            box.update_velocity_both(arg_list, firsts_p_ij_col)
            particle_coll_counters[firsts_p_ij_col[0]] += 1
            particle_coll_counters[firsts_p_ij_col[1]] += 1
        counter += 1

        t += dt

        if counter % print_every == 0:
            print(particle_coll_counters)
            print(particle_wall_counters)
            print("************************************")
            print(box)
            print("************************************")
            if (np.sum(particle_coll_counters)/2 + np.sum(particle_wall_counters)) % print_every != 0:
                raise Exception('not updating particle wall collisions properly')

    particle_board = np.zeros((10, 10)) #for box at range 10
    particle_index = 3
    for row_i in range(10):
        for col_i in range(10):
            particle_board[row_i][col_i] = box.mat_board[row_i][col_i][particle_index]
    plt.imshow(particle_board, cmap='hot')
    plt.colorbar()
    plt.show()

    plt.hist(box.vx_particle1_counter)
    plt.hist(box.vx_particle2_counter)
    plt.hist(box.vx_particle3_counter)
    plt.hist(box.vx_particle4_counter)
    plt.xlabel('velocity')
    plt.ylabel('probability')
    plt.title('vx_particle2_counter_hist')
    plt.legend(['particle 1', 'particle 2', 'particle 3', 'particle 4'])
    plt.show()

    plt.hist(box.vy_particle1_counter)
    plt.hist(box.vy_particle2_counter)
    plt.hist(box.vy_particle3_counter)
    plt.hist(box.vy_particle4_counter)
    plt.xlabel('velocity')
    plt.ylabel('probability')
    plt.title('vy_particle2_counter_hist')
    plt.legend(['particle 1', 'particle 2', 'particle 3', 'particle 4'])
    plt.show()

    plt.hist(box.vabs_particle1_counter)
    plt.hist(box.vabs_particle2_counter)
    plt.hist(box.vabs_particle3_counter)
    plt.hist(box.vabs_particle4_counter)
    plt.xlabel('velocity')
    plt.ylabel('probability')
    plt.title('v_tot_particle2_counter_hist')
    plt.legend(['particle 1', 'particle 2', 'particle 3', 'particle 4'])
    plt.show()
    print('finish')








import numpy as np
from Ex_5const import *


class IsingLattice:
    def __init__(self, J, T):
        self.J = J
        self.T = T
        self.size = 16
        self.lattice = np.random.choice([-1, 1], size=(self.size, self.size))  # Initialize the lattice randomly
        print("lattice", self.lattice)

    def calc_energy(self, i, j):
        """Calculates the energy of a single site (i, j)"""
        s = self.lattice[i, j]
        neighbors = (self.lattice[(i + 1) % self.size, j] + self.lattice[(i - 1) % self.size, j] +
                     self.lattice[i, (j + 1) % self.size] + self.lattice[i, (j - 1) % self.size])
        return -self.J * s * neighbors - h * s

    def calc_energy_for_all_lattice(self, factor=1):
        """Calculates the energy for_all_lattice"""

        right = np.roll(self.lattice, 1, axis=1)
        left = np.roll(self.lattice, -1, axis=1)
        down = np.roll(self.lattice, 1, axis=0)
        up = np.roll(self.lattice, -1, axis=0)

        all_lattice = (left + right + up + down)

        return - factor * self.J * self.lattice * all_lattice - h * self.lattice

    def p_flip(self, epsilon_now):
        return 1 / (np.exp(-2 * epsilon_now) + 1)

    def compute_p_flip_now(self):
        epsilon_now = self.calc_energy_for_all_lattice()
        p_flip_now = self.p_flip(epsilon_now)
        return p_flip_now

    def flip_spin_for_all(self):
        """Flips the spin at all the lattice"""
        torf = 0
        if np.random.rand() <= self.compute_p_flip_now:
            self.calc_energy_for_all_lattice *= -1
            torf = 1
            # print("s", self.lattice[i, j])
        return torf

    def flip_spin(self, i, j):
        """Flips the spin at site (i, j)"""
        torf = 0
        energy_diff = -2 * self.calc_energy(i, j)
        if np.random.rand() <= 1 / (np.exp(energy_diff) + 1):
            self.lattice[i, j] *= -1
            torf = 1
            # print("s", self.lattice[i, j])
        return torf

    def lattice_magnetization(self):
        """find the sum over s of the lattice"""
        m = 0
        for i in range(self.size):
            for j in range(self.size):
                m += self.lattice[i, j]
        return m

    def change_lattice_spins_step(self):
        p_flip_now = self.compute_p_flip_now()
        size = self.size
        p = np.random.uniform(0, 1, (size, size))
        torf = p <= p_flip_now
        total_num_of_flips = np.sum(torf)
        total_num_tries_to_flip = self.size ** 2
        self.lattice = (1 - 2 * torf) * self.lattice
        # the last line updates the lattice array by flipping the spin of certain particles.
        # It does this by creating a new array, which is a copy of the lattice array,
        # but with the correct particles multiplied by -1.
        return total_num_of_flips, total_num_tries_to_flip



#print('Beta =', h)

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

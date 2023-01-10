import numpy as np
from Ex_5const import *


class IsingLattice:
    def __init__(self, J, T):
        self.J = J
        self.T = T
        self.size = 16
        self.lattice = np.random.choice([-1, 1], size=(self.size, self.size))  # Initialize the lattice randomly

    def calc_energy(self, i, j):
        """Calculates the energy of a single site (i, j)"""
        s = self.lattice[i, j]
        neighbors = (self.lattice[(i + 1) % self.size, j] + self.lattice[(i - 1) % self.size, j] +
                     self.lattice[i, (j + 1) % self.size] + self.lattice[i, (j - 1) % self.size])
        return -self.J * s * neighbors - h*s

    def flip_spin(self, i, j):
        """Flips the spin at site (i, j)"""
        energy_diff = -2 * self.calc_energy(i, j)
        if np.random.rand() <= 1 / (np.exp(-energy_diff)+1):
            self.lattice[i, j] *= -1

    def simulate(self, steps):
        """Simulate the system for 'steps' number of steps"""
        for _ in range(steps):
            i, j = np.random.randint(0, 16, size=2)
            self.flip_spin(i, j)

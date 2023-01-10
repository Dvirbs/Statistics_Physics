import numpy as np
from Ex_5 import *
import numpy as np


def run_simulation(k, lattice_scan):
    # Initialize the lattice with random spin values
    lattice = IsingLattice(0.1, 1)
    magnetization_half_k = np.zeros(int(k * 0.5))

    # Run k/2 steps
    for _ in range(k // 2):
        lattice_scan += 1
        for x in range(16):
            for y in range(16):
                lattice.flip_spin(x, y)
            if lattice_scan % 3 == 0:
                magnetization_list.append(np.mean(self.lattice))

    # Document magnetization every 3 scans of the lattice
    for _ in range(3):
        magnetization.append(np.mean(lattice))
        for _ in range(k // 2):
            x, y = np.random.randint(0, 16, 2)
            lattice[x, y] *= -1

    mean_magnetization_k_2 = np.mean(magnetization)

    # Run k more times
    for _ in range(k):
        x, y = np.random.randint(0, 16, 2)
        lattice[x, y] *= -1

    # Document magnetization every 3 scans of the lattice
    magnetization = []
    for _ in range(3):
        magnetization.append(np.mean(lattice))
        for _ in range(k):
            x, y = np.random.randint(0, 16, 2)
            lattice[x, y] *= -1

    mean_magnetization_k = np.mean(magnetization)

    # check convergence
    if abs(mean_magnetization_k - mean_magnetization_k_2) / abs(mean_magnetization_k) < 1e-3 or k >= 10 ** 8:
        return True, mean_magnetization_k
    else:
        return False, mean_magnetization_k


# set k value
k = 16 * 16
lattice_scan = 0

while True:
    converged, mean_magnetization = run_simulation(k, lattice_scan)
    if converged:
        print("Converged! Mean magnetization:", mean_magnetization)
        break
    k *= 2

# import numpy as np
#
# class IsingLatticeConvergence:
#     def __init__(self, J, T, k):
#         self.J = J
#         self.T = T
#         self.lattice = np.random.choice([-1, 1], size=(16, 16))
#         self.k = k
#         self.magnetization_half_k = []
#         self.magnetization_full_k = []
#
#     def calc_energy(self, i, j):
#         """Calculates the energy of a single site (i, j)"""
#         s = self.lattice[i, j]
#         neighbors = (self.lattice[(i+1)%16, j] + self.lattice[(i-1)%16, j] +
#                      self.lattice[i, (j+1)%16] + self.lattice[i, (j-1)%16])
#         return -self.J * s * neighbors
#
#     def flip_spin(self, i, j):
#         """Flips the spin at site (i, j)"""
#         energy_diff = -2 * self.calc_energy(i, j)
#         if energy_diff <= 0 or np.random.rand() < np.exp(-energy_diff / self.T):
#             self.lattice[i, j] *= -1
#
#     def simulate(self):
#         """Simulate the system for 'steps' number of steps"""
#         k_2 = self.k * 0.5
#         for step in range(int(self.k)):
#             i, j = np.random.randint(0, 16, size=2)
#             self.flip_spin(i, j)
#             if 0.25 <= step / k_2 < 0.5:
#                 magnetization = np.mean(self.lattice)
#                 self.magnetization_half_k.append(magnetization)
#                 if step % 3 == 0:
#                     print(f"Magnetization after {step} steps: {magnetization}")
#             elif 0.5 <= step / k_2 < 1:
#                 magnetization = np.mean(self.lattice)
#                 self.magnetization_full_k.append(magnetization)
#                 if step % 3 == 0:
#                     print(f"Magnetization after {step} steps: {magnetization}")
#             mean_magnetization_half_k = np.mean(self.magnetization_half_k)
#             mean_magnetization_full_k = np.mean(self.magnetization_full_k)
#             if abs(mean_magnetization_half_k - mean_magnetization_full_k) / abs(mean_magnetization_full_k) < 10 ** -3 or step == 10 ** 8:
#                 print(f"Convergence reached after {step} steps with mean magnetization {mean_magnetization_full_k}")
#                 break

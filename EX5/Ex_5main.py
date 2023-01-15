from Ex_5 import *
import numpy as np
import time


def run_simulation(k, lattice, mean_magnetization_k_2):
    # Initialize the lattice with random spin values
    magnetization_half_k = np.zeros(int(k * 0.5))
    magnetization_k = np.zeros(int(k))
    U_list = []
    flip = 0
    lattice_scan = 0

    if mean_magnetization_k_2 is None:
        # Run k/2 flips without documenting
        while flip < k / 2:
            for x in range(16):
                for y in range(16):
                    torf = lattice.flip_spin(x, y)
                    flip += torf
                    # print('k', k, 'torf', torf)
            if flip > k / 2:
                flip = k / 2

        # Run k/2 flips while documenting
        while k / 2 <= flip < k:
            lattice_scan += 1
            m = 0
            for x in range(16):
                for y in range(16):
                    torf = lattice.flip_spin(x, y)
                    flip += torf
                    m += lattice.lattice[x, y]
            if lattice_scan % n_sweep == 0:
                magnetization_half_k[(int(lattice_scan / n_sweep) - 1)] = m
                #print("magnetization_half_k[step] = ", magnetization_half_k[(int(lattice_scan / n_sweep) - 1)])
                # TODO check if the vector starting from 0
            if flip > k:
                flip = k

        mean_magnetization_k_2 = np.sum(magnetization_half_k) / ((lattice_scan + 1) / n_sweep)
    else:
        flip = k

    # Run k more times
    lattice_scan = 0
    while flip <= 2 * k:
        lattice_scan += 1
        m = 0
        e = 0

        for x in range(16):
            for y in range(16):
                torf = lattice.flip_spin(x, y)
                flip += torf
                m += lattice.lattice[x, y]
                e += lattice.calc_energy(x, y)  # calculate the energy of particle [x,y]

        if lattice_scan % n_sweep == 0:
            magnetization_k[(int(lattice_scan / n_sweep) - 1)] = m  # same
            # print("magnetization_k[step] = ", magnetization_k[(int(lattice_scan / n_sweep) - 1)])
            U_list.append(e)

    mean_magnetization_k = np.sum(magnetization_k) / ((lattice_scan + 1) / n_sweep)
    mean_magnetization_square_k = np.sum(magnetization_k ** 2) / ((lattice_scan + 1) / n_sweep)
    average_U_K = np.mean(U_list)
    average_U_squared_K = np.mean(np.array(U_list) ** 2)
    # check convergence

    print('delta = ', abs(mean_magnetization_k - mean_magnetization_k_2) / abs(mean_magnetization_k))
    if abs(mean_magnetization_k - mean_magnetization_k_2) / abs(mean_magnetization_k) < 1e-3 or k >= 10 ** 8:
        return True, mean_magnetization_k, mean_magnetization_square_k, average_U_K, average_U_squared_K
    else:
        return False, mean_magnetization_k, mean_magnetization_square_k, average_U_K, average_U_squared_K


# set k value
k = 16 * 16 * 3 * 100
lattice = IsingLattice(0.1, 1)
mean_magnetization_k_2 = None

while True:
    converged, mean_magnetization, mean_magnetization_square_k, average_U_K, average_U_squared_K = run_simulation(k,
                                                                                                                  lattice,
                                                                                                                  mean_magnetization_k_2)
    if converged:
        print("Converged! Mean magnetization:", mean_magnetization)
        print("Converged! Mean mean_magnetization_square_k:", mean_magnetization_square_k)
        print("Converged! Mean mean_magnetization_square_k:", mean_magnetization_square_k)
        print("Converged! average_U_K:", average_U_K)
        print("Converged! average_U_squared_K:", average_U_squared_K)
        break
    k *= 2
    print('re running, k = ', k)
    mean_magnetization_k_2 = mean_magnetization

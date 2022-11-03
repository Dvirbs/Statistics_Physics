# Ex 2 Statistics
# Dvir and Noa
import math
import random
import matplotlib.pyplot as plt


# Part A

# Q 2a
def initial_state(n, q, g):
    """
    We will define the initial parameters and we will give random q energy level for each of the
    N_a particles at A
    :return: We will return Grope A [List]
    """
    for j in range(q):
        i = random.randint(1, n)
        g[i - 1] += 1
    return g


# Q 2b
def two_solids(steps, n, g):
    """
    Calculate the changes in two solids מצומדים
    and calculate the total energy in each solid
    :return: Two list that is represent the two solids, and two list of the energy of each solid in each step
    """
    q_A = list()
    q_B = list()
    in_correct_energy_direction = 0
    for step in range(steps):
        i = random.randint(1, n)
        j = random.randint(1, n)
        if 0 < g[i - 1]:
            g[i - 1] -= 1
            g[j - 1] += 1
        q_a_step = sum(g[:100])  # group A is g[:100]
        q_A.append(q_a_step)
        q_B.append(300 - q_a_step)
        if (i <= 100 and q_a_step < 150) or (
                100 < i and 150 < q_a_step):  # if we move energy from A to B (i<100) and Solid A have les energy
            in_correct_energy_direction += 1

    g_A = g[:100]
    g_B = g[100:200]
    return g_A, g_B, q_A, q_B, in_correct_energy_direction


def energy_steps_graph(q1, q2, steps):
    plt.plot([i for i in range(1, steps + 1)], q1)
    plt.plot([i for i in range(1, steps + 1)], q2)
    plt.xscale('log')
    plt.xlabel('Log Step(time)')
    plt.ylabel('Energy_Level')
    plt.title("Linear graph")
    plt.show()


# Part 2
def bath_and_solid(steps, g):
    """

    :return:
    """
    energy_g = list()
    energy_q23 = list()
    for step in range(steps):
        i = random.randint(1, 100)
        delta = random.randrange(-1, 2, 2)
        if delta == -1:
            if g[i - 1] > 0:
                g[i - 1] -= 1
        else:
            p = random.uniform(0, 1)
            if p <= math.exp(-1 / theta):
                g[i - 1] += 1
        tot_energy = sum(g)
        energy_g.append(tot_energy)
        energy_q23.append(g[23])
    return g, energy_g, energy_q23

def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
     return hist


if __name__ == '__main__':
    N_A = 100
    N_B = 100
    N = N_A + N_B
    Q_A = 300
    A = [0] * N_A
    B = [0] * N_B
    A = initial_state(N_A, Q_A, A)
    AB = A + B
    STEPS = 10 ** 5
    A, B, q_A, q_B, in_correct_energy_direction = two_solids(STEPS, N, AB)
    energy_steps_graph(q_A, q_B, STEPS)

    # Part 2
    N_C = 100
    C = [0] * N_C
    theta = 2.5
    STEPS = 10 ** 7
    C, energy_C, energy_C23 = bath_and_solid(STEPS, C)



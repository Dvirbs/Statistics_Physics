# Ex 2 Statistics
# Dvir and Noa
import math
import random
import matplotlib.pyplot as plt
import numpy


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
    # plt.xscale('log')
    plt.xlabel('Step(time)')
    plt.ylabel('Energy_Level')
    plt.title("Linear graph")
    plt.show()


# Part 2
def hist(g, step, bins):
    h = plt.hist(g, bins=range(bins))
    plt.clf()
    return h


def plot_hist(h):
    #plt.plot(numpy.arange(20), numpy.array(h[0]) / 100)
    plt.plot(numpy.arange(20), numpy.array(h[0]))
    #plt.plot(numpy.arange(20), numpy.array(h[1]) / 100)
    plt.plot(numpy.arange(20), numpy.array(h[1]))
    # plt.plot(numpy.arange(20), numpy.array(h[2]) / 100)
    plt.plot(numpy.arange(20), numpy.array(h[2]))
    # plt.plot(numpy.arange(20), numpy.array(h[3]) / 100)
    plt.plot(numpy.arange(20), numpy.array(h[3]))
    # plt.plot(numpy.arange(20), numpy.array(h[4]) / 100)
    plt.plot(numpy.arange(20), numpy.array(h[4]))
    plt.legend(['2*10^6', '4*10^6', '6*10^6', '8*10^6', '10^7'])
    plt.title("Numbers of Particles Each Energy histogram")
    plt.yscale('log')
    plt.xlabel('Energy Levels')
    plt.ylabel('Numbers of Particles[Norm]')
    plt.show()


def bath_and_solid(steps, g, n_g):
    """
    :return:
    """
    energy_g = list()
    energy_q23 = list()
    hist_different_steps = list()
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
        if step == 2 * 10 ** 6 or step == 4 * 10 ** 6 or step == 6 * 10 ** 6 or step == 8 * 10 ** 6 or step == 10 ** 7 - 1:
            h = hist(g, step, 21)
            hist_different_steps.append(h[0])
    plot_hist(hist_different_steps)
    return g, energy_g, energy_q23


def energy_steps_graph_Q_tot(q, steps):
    step_axis = numpy.array([i for i in range(1, steps + 1)])
    plt.plot(step_axis, q)
    plt.xscale('log')
    plt.xlabel('Step(Time)')
    plt.ylabel('Energy_Level')
    plt.title("Change of Energy Level Solid Per Step")
    plt.show()


def energy_steps_graph_Q23(q, steps):
    h = plt.hist(q, bins=20)
    plt.clf()
    plt.plot(numpy.arange(20), numpy.array(h[0]/10**7))
    plt.xlabel('Energy_Level')
    plt.ylabel('step - norm')
    plt.title("energy histogram for particle num 23")
    plt.show()


def energy_steps_graph_Q23_log(q, steps):
    step_axis = numpy.array([i for i in range(1, steps + 1)]) / (10 ** 7)
    plt.plot(step_axis, q)
    plt.xscale('log')
    plt.xlabel('Step(Time-log)')
    plt.ylabel('Energy_Level')
    plt.title("Change of Energy Level Of Particle  Per Step")
    plt.show()


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
    print("in_correct_energy_direction", in_correct_energy_direction)
    # Part 2
    N_C = 100
    C = [0] * N_C
    theta = 2.5
    STEPS = 10 ** 7
    C, energy_C, energy_C23 = bath_and_solid(STEPS, C, N_C)
    energy_steps_graph_Q_tot(energy_C, STEPS)
    energy_steps_graph_Q23(energy_C23, STEPS)
    energy_steps_graph_Q23_log(energy_C23, STEPS)
    # hist(energy_C23, STEPS, 25)

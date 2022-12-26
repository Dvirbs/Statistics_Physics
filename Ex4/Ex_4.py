import math

from Ex_4_const import *
import numpy as np
import random


class U_Levels:

    g_calc = np.zeros(101)  # Caching of possible degredation values
    def __init__(self):

        for n in range(0,101):
            self.g_calc[n] = 0.5 * n * (n + 3) + 1

        U_store = self.U_initial_state()
        print('U_store', U_store)
        self.n_bottom = np.zeros(n_max)
        self.n_top = np.zeros(n_max)

        for n_i, n in enumerate(U_store):
            if n == 0:
                self.n_bottom[n_i] = 0
                self.n_top[n_i] = 0
            else:
                self.n_bottom[n_i] = sum(U_store[:n_i]) + 1
                self.n_top[n_i] = self.n_bottom[n_i] + n - 1  # n_top is the highest particle at the n level. n = n_t - n_b + 1

    def U_initial_state(self):
        U_store = np.zeros(n_max)
        for i in range(N):
            Ur_i = random.randint(0, 99)
            U_store[Ur_i] += 1
        return U_store


def myu_binary_search_Step(N, n_max, T):
    myu_min = -30
    myu_max = 0
    N_try = -1
    while int(N_try) != N:
        myu_try = 0.5 * (myu_min - myu_max) + myu_max

        N_try = 0.0
        for n in range(0, n_max + 1):
            if (n - myu_try) / T < 50:
                N_try += U_Levels.g_calc[n] / (np.exp((n - myu_try) / T) - 1)
            else:
                break

#        N_try = np.sum([g_calculation(n) / (np.exp((n - myu_try) / T) - 1) for n in range(0, n_max + 1)])
        if N < N_try:
            myu_max = myu_try
        else:
            myu_min = myu_try
    return myu_try


# def g_calculation(n: int):
# #    g = 0.5 * n * (n + 3) + 1
# #    return g
#     return U_Levels.g_calc[n]

def energy_minus_probability(n, t, myu):
    p = random.uniform(0, 1)
    g_n_plus = U_Levels.g_calc[n + 1]
    g_n_minus = U_Levels.g_calc[n - 1]
    if n == 0:
        threshold = 0.0098  # choose a small threshold value
        if abs(- myu) / t < threshold:
            # set p_n_minus to some default value (e.g., 0)
            p_n_minus = 1
        else:
            # calculate p_n_minus as before
            g_n_zeros = U_Levels.g_calc[n]
            factor_gibbs_zero = np.exp((- myu) / t)
            p_n_minus = (g_n_zeros / (factor_gibbs_zero - 1)) / (
                    g_n_plus / (np.exp((1 - myu) / t) - 1) + g_n_zeros / (factor_gibbs_zero - 1))
    else:
        threshold = 0.0098  # choose a small threshold value
        if abs(n - 1 - myu) / t < threshold:
            # set p_n_minus to some default value (e.g., 0)
            p_n_minus = 1
        else:
            factor_gibbs_n_minus_1 = np.exp((n - 1 - myu) / t)
            p_n_minus = (g_n_minus / (factor_gibbs_n_minus_1 - 1)) / (
                        g_n_plus / (np.exp((n + 1 - myu) / t) - 1) + g_n_minus / (factor_gibbs_n_minus_1 - 1))
    if p <= p_n_minus:
        energy_minus = 1
    else:
        energy_minus = 0
    return energy_minus


# if __name__ == '__main__':
#     myu = myu_binary_search_Step(1000, n_max, 0.2)
#     print("myu for N = 1000", myu)
#     myu = myu_binary_search_Step(10000, n_max, 0.2)
#     print("myu for N = 10000---Myu need to be smaller!", myu)

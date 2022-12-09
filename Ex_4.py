from Ex_4_const import *
import numpy as np
import random


class U_Levels:
    """

    """

    def __init__(self):
        U_store = self.U_initial_state()
        print('U_store', U_store)
        print('U_store sum', sum(U_store))
        self.n_bottom = np.zeros(n_max)
        self.n_top = np.zeros(n_max)
        for n_i, n in enumerate(U_store):
            if n == 0:
                self.n_bottom[n_i] = n
                self.n_top[n_i] = n
            else:
                self.n_bottom[n_i] = sum(U_store[:n_i]) + 1
                self.n_top[n_i] = self.n_bottom[n_i] + n - 1  # n_top is the highest particle at the n level. n = n_t - n_b + 1


    def U_initial_state(self):
        U_store = np.zeros(n_max)
        for i in range(N):
            Ur_i = random.randint(0, 99)
            U_store[Ur_i] += 1
        return U_store


if __name__ == '__main__':
    u_level = U_Levels()
    print('n_bottom', u_level.n_bottom)
    print('u_level.n_top', u_level.n_top)

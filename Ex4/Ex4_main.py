from Ex_4 import *
import numpy as np
import math

for t in np.arange(T_min, T_max + 0.2, 0.2):
    step = 0
    U = U_Levels()
    my = myu_binary_search_Step(N, n_max, t)
    while step < 1:  # for now
        # TODO change the step definition
        N_i = random.randint(1, N) # random particle
        bot_2_top = [str(math.floor(x)) + '-' + str(math.floor(y)) for x, y in zip(U.n_bottom, U.n_top)]
        for i in range(0, len(bot_2_top), 10):
            print(*bot_2_top[i:i + 10])
        p_b = max(np.where(U.n_bottom <= N_i, U.n_bottom, U.n_bottom != 0))
        p_b_i = np.where(p_b == U.n_bottom)[0][0]
        part_level_i = np.where(N_i <= U.n_top)[0][0]
        if part_level_i == p_b_i:
            print('yay!!!')
            print("p_b= ", p_b)
            print("p_n= ", U.n_top[part_level_i])
        P_minus = energy_minus_probability(part_level_i, t, my)  # true or false for n-1
        # TODO always P_minus=1?
        if P_minus:
            U.n_top[part_level_i - 1] = U.n_bottom[part_level_i]
            if U.n_bottom[part_level_i - 1] == 0:
                U.n_bottom[part_level_i-1] = U.n_bottom[part_level_i]
            if U.n_bottom[part_level_i] == U.n_top[part_level_i]:
                U.n_bottom[part_level_i] = U.n_top[part_level_i] = 0
            else:
                U.n_bottom[part_level_i] += 1
        else:
            if part_level_i == 100:
                continue
            U.n_bottom[part_level_i + 1] = U.n_top[part_level_i]
            if U.n_top[part_level_i + 1] == 0:
                U.n_top[part_level_i + 1] = U.n_top[part_level_i]
            if U.n_top[part_level_i] == U.n_bottom[part_level_i]:
                U.n_bottom[part_level_i] = U.n_top[part_level_i] = 0
            else:
                U.n_top[part_level_i] -= 1


        print("P_minus= ", P_minus)
        print('bot_2_top_loop:')
        bot_2_top = [str(math.floor(x)) + '-' + str(math.floor(y)) for x, y in zip(U.n_bottom, U.n_top)]
        for i in range(0, len(bot_2_top), 10):
            print(*bot_2_top[i:i + 10])
        step += 1

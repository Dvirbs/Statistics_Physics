from Ex_4 import *
import numpy as np
import matplotlib.pyplot as plt

t_vector = np.arange(T_min, T_max, 0.2)
N0_mean_per_t = np.zeros(np.size(t_vector))
N0_squared_mean_per_t = np.zeros(np.size(t_vector))
U_tot_mean = np.zeros(np.size(t_vector))
c_v = np.zeros(np.size(t_vector))
# print(N0_mean_per_t)

for t_i, t in enumerate(t_vector):
    U = U_Levels()
    my = myu_binary_search_Step(N, n_max, t)
    # פרמטרים עבור ההתכנסות
    k = 10 ** 6
    k_2 = k * 2
    N0_half_k = np.zeros(int(k * 0.5))
    N0_full_k = np.zeros(int(k))
    U_tot = np.zeros(int(k))
    U_tot_sum = sum([(U.n_top[n] - U.n_bottom[n] + 1) * n for n in range(0, n_max - 1) if U.n_top[n] != 0])
    U_last_temp = U_tot_sum
    delta_cal = 1000
    if t <= 1:
        delta = 10 ** -3
    elif 1 < t <= 2:
        delta = 5 * (10 ** -3)
    else:
        delta = 10 ** -2
    # delta = 1000 - 10
    # delta_cal = random.randint(1, 1000)
    step = 1

    while delta <= delta_cal:
        N_i = random.randint(1, N)  # random particle
        # bot_2_top = [str(math.floor(x)) + '-' + str(math.floor(y)) for x, y in zip(U.n_bottom, U.n_top)]
        # for i in range(0, len(bot_2_top), 10):
        #     print(*bot_2_top[i:i + 10])
        # p_b = max(np.where(U.n_bottom <= N_i, U.n_bottom, U.n_bottom != 0))
        # p_b_i = np.where(p_b == U.n_bottom)[0][0]
        # part_level_i = np.where(N_i <= U.n_top)[0][0]
        part_level_i = np.argmax(U.n_top >= N_i)

        # if part_level_i != p_b_i:
        #      print('yay!!!')
        #     print("p_b= ", p_b)
        #     print("p_n= ", U.n_top[part_level_i], "part_level_i", part_level_i)
        #     raise Exception("something wrong with the energy level")
        P_minus = energy_minus_probability(part_level_i, t, my)  # true or false for n-1
        if P_minus:
            if part_level_i != 0:
                U_last_temp -= 1
                U_tot_sum += U_last_temp
                U.n_top[part_level_i - 1] = U.n_bottom[part_level_i]
                if U.n_bottom[part_level_i - 1] == 0:
                    U.n_bottom[part_level_i - 1] = U.n_bottom[part_level_i]
                if U.n_bottom[part_level_i] == U.n_top[part_level_i]:
                    U.n_bottom[part_level_i] = U.n_top[part_level_i] = 0
                else:
                    U.n_bottom[part_level_i] += 1
        else:
            if part_level_i != 99:  # python !!!!
                U_last_temp += 1
                U_tot_sum += U_last_temp
                U.n_bottom[part_level_i + 1] = U.n_top[part_level_i]
                if U.n_top[part_level_i + 1] == 0:
                    U.n_top[part_level_i + 1] = U.n_top[part_level_i]
                if U.n_top[part_level_i] == U.n_bottom[part_level_i]:
                    U.n_bottom[part_level_i] = U.n_top[part_level_i] = 0
                else:
                    U.n_top[part_level_i] -= 1

        # תנאיים עבור ההתנכסות
        if 0.25 <= step / k_2 < 0.5:
            if U.n_top[part_level_i] == U.n_bottom[part_level_i]:
                N0_half_k[-(k - step)] = 1
            else:
                N0_half_k[-(k - step)] = U.n_top[part_level_i] - U.n_bottom[part_level_i]
        elif 0.5 <= step / k_2 < 1:
            if U.n_top[part_level_i] == U.n_bottom[part_level_i]:
                N0_full_k[step - k] = 1
            else:
                N0_full_k[step - k] = U.n_top[part_level_i] - U.n_bottom[part_level_i]
        elif k_2 / step == 1:
            N0_full_k_mean = np.mean(N0_full_k)
            delta_cal = abs(N0_full_k_mean - np.mean(N0_half_k)) / N0_full_k_mean
            print("delta_cal", delta_cal)
            if delta_cal <= delta:
                print("t = ", t)
                break
            else:
                k = k * 2
                k_2 = k * 2
                N0_half_k = N0_full_k
                N0_full_k = np.zeros(int(k))
                U_tot_sum = 0
        if (step % 100000 == 0):
            print("step = ", step, "temperature = ", t)
        # print("t = ", t)
        # print("k_2 = ", k_2, "step = ", step)
        # print("P_minus= ", P_minus)
        # print('bot_2_top_loop:')
        # bot_2_top = [str(math.floor(x)) + '-' + str(math.floor(y)) for x, y in zip(U.n_bottom, U.n_top)]
        # for i in range(0, len(bot_2_top), 10):
        #     print(*bot_2_top[i:i + 10])
        step += 1
    N0_mean_per_t[t_i] = np.mean(N0_full_k)
    N0_squared_mean_per_t[t_i] = np.mean(N0_full_k ** 2)
    U_tot_mean[t_i] = U_tot_sum / k
    if step == k_2:
        U_tot_mean[t_i] = U_tot_sum / k_2
    c_v[t_i] = U_tot_mean[t_i] / (N * t)

print(N0_mean_per_t)
print(U_tot_mean)
print(c_v)
standard_deviation = (N0_squared_mean_per_t - N0_mean_per_t ** 2) ** 0.5
print(standard_deviation)
plt.plot(t_vector, N0_mean_per_t / N)
plt.errorbar(t_vector, N0_mean_per_t / N, yerr=standard_deviation / N0_mean_per_t)
# plt.xscale('log')
plt.xlabel('temperature')
plt.ylabel('<N0>/N')
plt.title("<N_0>(T)/N for N = {}".format(N))
plt.show()

plt.plot(t_vector, c_v)
plt.xlabel('temperature')
plt.ylabel('c_v')
plt.title("c_v(t) for N = {}".format(N))
plt.show()


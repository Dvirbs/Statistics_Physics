from Ex_5 import *
import numpy as np


class IsingExperiment:
    def __init__(self, h, lattice, K=k):
        self.mean_M_K_2 = None
        self.mean_M_K = None
        self.mean_M_squared_K = None
        self.mean_U_K = None
        self.mean_U_squared_K = None
        self.K = K
        self.flip = 0
        self.total_num_tries_to_flip = 0
        self.lattice = lattice
        self.flip_ratio = None
        self.h = h

    def get_current_M(self):
        M = np.sum(self.lattice.lattice)
        return M

    def get_current_U(self):
        epsilon_now = self.lattice.calc_energy_for_all_lattice(factor=0.5)  # עבור האנרגיות צריך פקטור חצי
        U = np.sum(epsilon_now)
        return U

    def energy_variance(self):
        value = self.mean_U_squared_K - self.mean_U_K ** 2
        return value

    def specific_heat_capacity(self):
        energy_std = self.energy_variance()
        return np.sqrt(energy_std) / (self.lattice.size ** 2)

    def print_step_in_running_process(self, which_k):
        if self.flip % 10000 == 0:
            print(f"flip Current step: {self.flip}")
            print(f"K Current step: {self.K}")
            print("lattice", self.lattice.lattice)
            print(which_k)

    def run_k_divide_2_steps(self):
        self.flip = 0
        self.total_num_tries_to_flip = 0
        magnetization_list = []

        while self.flip < self.K // 2:
            self.print_step_in_running_process('while loop of K // 2')
            for _ in range(n_sweep):
                total_num_of_flips, total_num_tries_to_flip = self.lattice.change_lattice_spins_step()
                self.flip += total_num_of_flips
                self.total_num_tries_to_flip += total_num_tries_to_flip

            current_M = self.get_current_M()
            magnetization_list.append(current_M)
        # הודיה שמה את השורה הבאה של מיצוע על המגנטיזציה בתור ה WHILE אבל חשבתי שאין צורך
        self.mean_M_K_2 = np.mean(magnetization_list)
        # אנחנו חישבנו את הממוצע בצורה אחרת לפיה שורה הבאה:
        # mean_magnetization_k_2 = np.sum(magnetization_half_k) / ((lattice_scan + 1) / n_sweep)

    def run_k_steps(self):
        magnetization_list = []
        energies_list = []

        while self.flip <= 2 * self.K:
            self.print_step_in_running_process('while loop of K ')

            for _ in range(n_sweep):
                total_num_of_flips, total_num_tries_to_flip = self.lattice.change_lattice_spins_step()
                self.flip += total_num_of_flips
                self.total_num_tries_to_flip += total_num_tries_to_flip
            current_M = self.get_current_M()
            magnetization_list.append(current_M)
            current_U = self.get_current_U()
            energies_list.append(current_U)
        self.flip_ratio = self.flip / self.total_num_tries_to_flip
        self.mean_M_K = np.mean(magnetization_list)
        self.mean_M_squared_K = np.mean(np.array(magnetization_list) ** 2)
        self.mean_U_K = np.mean(energies_list)
        self.mean_U_squared_K = np.mean(np.array(energies_list) ** 2)

    def converged(self):
        convergence_value = np.abs(self.mean_M_K - self.mean_M_K_2) / (1e-8 + np.abs(self.mean_M_K))
        # הודיה הכניסה המספר 1e-8 במכנה ואנחנו לא, כנראה בשביל למנוע מכך שהמכנה יהיה מספר קטן מדי
        # print(f"convergence_value = {convergence_value}")
        return convergence_value <= delta or 10 ** 8 <= self.K

    def run(self):
        self.run_k_divide_2_steps()
        self.run_k_divide_2_steps()  # לא צריך לאפס את הנתונים מהריצה הקודמת (run_k_divide_2_steps) מכיוון שכל פעם אנו יוצרים אותם מחדש

        self.flip = 0  # # אנחנו לא איפסנו את ה flip אלא הגדרנו אותו להיות שווה ל K
        # אני חושב שזה יותר נכון בגלל החלוקה לפונקציות run_k_divide_2_steps ו run_k_steps שעבור כל אחד נספור את ה flip בנפרד

        self.total_num_tries_to_flip = 0

        self.run_k_steps()

        while not self.converged():
            self.mean_M_K_2 = self.mean_M_K
            self.K *= 2
            print("K", self.K)
            self.run_k_steps()


def single_experiment(h, J):
    lattice = IsingLattice(J, 1)
    experiment = IsingExperiment(h, lattice)
    experiment.run()
    Data = {
        "h": experiment.h,
        "J": lattice.J,
        "K": experiment.K,
        "<M>": experiment.mean_M_K,
        "<M^2>": experiment.mean_M_squared_K,
        "std": experiment.energy_variance(),
        "<U>": experiment.mean_U_K,
        "<U^2>": experiment.mean_U_squared_K,
        "cv": experiment.specific_heat_capacity(),
        "flip_ratio": experiment.flip_ratio,
    }
    print(Data)
    return Data


if __name__ == '__main__':
    # set k value
    J = 0.1
    All_Data = []
    while J < 0.8:
        J += 0.05
        data = single_experiment(h, J)
        print(J)
        All_Data.append(data)

    print(All_Data)

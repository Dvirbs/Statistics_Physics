import matplotlib.pyplot as plt
import numpy as np

# Assuming you have a list of J values and a corresponding list of energy values
J_values = np.arange(0.1, 0.50, 0.05)

U = [-262.12344497607654,-296.86463519313304,-331.40656506447834,-363.5756770310933,-394.55213308290854,-424.15697926059516,-452.99224586288426,-480.7798978460564]
U_square = [68819.20918660286,88233.22898712447,109914.21111371632,132257.0727808425,155725.9452374564,179951.60206717768,205234.25989598114,231172.621628326]


def specific_heat_capacity():
    energy_std = np.array(U_square) - np.array(U) ** 2
    return energy_std / (16 ** 2)


def energy_graph():
    import matplotlib.pyplot as plt

    # Generate data for energy and energy squared
    j_values = J_values
    energy_values = np.array(U)**2
    energy_squared_values = U_square

    # Create a figure and axes
    fig, ax = plt.subplots()

    # Plot energy values
    ax.plot(j_values, energy_values, label='Energy')

    # Plot energy squared values
    ax.plot(j_values, energy_squared_values, label='Energy Squared')

    # Add labels and legend
    ax.set_xlabel('J')
    ax.set_ylabel('Energy')
    ax.legend()

    # Show the figure
    plt.show()


def capacity_graph():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(J_values, specific_heat_capacity())

    # Add labels to the axes
    ax.set_xlabel("J values")
    ax.set_ylabel("specific_heat_capacity values")

    # Add a title to the plot
    ax.set_title("specific_heat_capacity values vs J values")

    # Show the plot
    plt.show()


if __name__ == '__main__':
    capacity_graph()

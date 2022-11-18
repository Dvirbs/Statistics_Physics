# Dvir Ben Simchon and Noa Goldberg
# Ex 3 - Statistics


class Particle:
    """
    class that describe the particle data
    """

    def __init__(self, name: str, location: tuple, velocity: tuple, dt_wall: tuple):
        """
        A constructor for a Particle object
        :param name: A string representing the particle's name
        :param location:  tuple representing the particle's (x, y) location
        :param velocity: tuple representing the particle's (v_x, v_y) velocity
        """
        self.radius = 0.15
        self.name = name
        self.location = location
        self.velocity = velocity
        self.dt_wall = dt_wall


class Board:
    """
    class that represent the board
    """

    def __init__(self):
        """

        """
        self.particles = []
        self.mat_board = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    def update_dt_wall(self):
        """

        :return:
        """
        for particle in self.particles:
            for i in range(2):
                if particle.velocity[i] > 0:
                    particle.dt_wall[i] = (1 - particle.location[i] - particle.radius) / particle.velocity[i]
                if particle.velocity[i] < 0:
                    particle.dt_wall[i] = (particle.location[i] - particle.radius) / particle.velocity[i]


def fastest_particle_and_min_time(part1, part2, part3, part4) -> list[float, Particle, int]:
    list_dt_wall = [part1.dt_wall[0], part1.dt_wall[1], part2.dt_wall[0], part2.dt_wall[1], part3.dt_wall[0],
                    part3.dt_wall[1], part4.dt_wall[0], part4.dt_wall[1]]
    i = int(min(range(len(list_dt_wall)), key=list_dt_wall.__getitem__))
    dt_fast = list_dt_wall[i]
    fast_part = i // 2 +1
    if int(i/2):
        p_axis = 0
    else:
        p_axis = 1
    return [dt_fast, fast_part, p_axis]


if __name__ == '__main__':
    p1 = Particle("p1", (0.25, 0.25), (0.21, 0.12), (0, 0))
    p2 = Particle("p2", (0.25, 0.75), (0.78, 0.34583), (0, 0))
    p3 = Particle("p3", (0.75, 0.25), (-0.23, -0.79), (0, 0))
    p4 = Particle("p4", (0.75, 0.75), (0.71, 0.18), (0, 0))
    t = 0
    counter = 0
    box = Board()
    box.particles = [p1, p2, p3, p4]
    while counter <= 10**7:
        box.update_dt_wall()
        dt_coll = (0, 0)
        # TODO dt_coll
        dt, fastest_p, axis = fastest_particle_and_min_time(p1, p2, p3, p4)
        for p in box.particles:
            p.location[0], p.location[1] = p.location[0] + dt * p.velocity[0], p.location[1] + dt * p.velocity[1]
        # TODO change location of particles in board
        fastest_p.velocity[axis] = fastest_p.velocity[axis] * (-1)
        counter += 1





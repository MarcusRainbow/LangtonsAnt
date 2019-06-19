import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import List

X_SIZE = 100
Y_SIZE = 100

def move_ant(ant: (int, int, int, int),
    universe: List[List[bool]]) -> (int, int, int, int):

    x = ant[0]
    y = ant[1]
    x_dir = ant[2]
    y_dir = ant[3]

    # colour change
    old = universe[x][y]
    universe[x][y] = not old
    if old:
        # turn left
        was_x = x_dir
        x_dir = -y_dir
        y_dir = was_x
    else:
        # turn right
        was_x = x_dir
        x_dir = y_dir
        y_dir = -was_x

    # step
    x = (x + x_dir) % X_SIZE
    y = (y + y_dir) % Y_SIZE

    return (x, y, x_dir, y_dir)

def evolve(animate: bool):
    universe = numpy.zeros((X_SIZE, Y_SIZE), dtype=bool)

    # start from (50,50)
    mid_x = X_SIZE // 2
    mid_y = Y_SIZE // 2
    ants = [
        (mid_x + 0, mid_y + 1, 0, 1),
        (mid_x + 1, mid_y + 0, 1, 0),
        (mid_x + 0, mid_y - 1, 0, -1),
        #(mid_x - 1, mid_y + 0, -1, 0),
        ]

    fig = plt.figure()
    plt.axis("off")
    frames = []

    for _ in range(10000):
        if animate:
            frames.append((plt.imshow(universe, cmap='binary'),))

        for i in range(len(ants)):
            ants[i] = move_ant(ants[i], universe)

    if animate:
        animation.ArtistAnimation(fig, frames, interval=25, blit=True,
                                repeat_delay=1000)
    else:
        plt.imshow(universe, cmap='binary')

    plt.show()

if __name__ == '__main__':
    evolve(True)
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import List

X_SIZE = 30
Y_SIZE = 30
Z_SIZE = 30

def project(universe: List[List[List[bool]]]):

    projection = numpy.zeros((X_SIZE, Y_SIZE), dtype=int)
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            for k in range(Z_SIZE):
                if universe[i][j][k]:
                    projection[i][j] += 1

    return plt.imshow(projection, cmap='binary')

def evolve(animate: bool):
    universe = numpy.zeros((X_SIZE, Y_SIZE, Z_SIZE), dtype=bool)

    # start from (10,10,10)
    x = X_SIZE // 2
    y = Y_SIZE // 2
    z = Z_SIZE // 2
    move = (1, 0, 0)
    up = (0, 0, 1)
    prev = False

    fig = plt.figure()
    plt.axis("off")
    frames = []

    for _ in range(100):
        if animate:
            frames.append((project(universe),))

        # colour change in the cell we are sitting on
        old = universe[x][y][z]
        universe[x][y][z] = not old

        # if the colour changed from where we were last, rotate
        if prev != old:
            up = numpy.cross(up, move)

        # always turn left
        move = numpy.cross(move, up)

        # step forward one step
        x = (x + move[0]) % X_SIZE
        y = (y + move[1]) % Y_SIZE
        z = (z + move[2]) % Z_SIZE

    if animate:
        animation.ArtistAnimation(fig, frames, interval=25, blit=True,
                                repeat_delay=1000)
    else:
        project(universe)

    plt.show()

if __name__ == '__main__':
    evolve(True)
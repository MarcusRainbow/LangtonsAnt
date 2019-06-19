import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def evolve():
    X_SIZE = 100
    Y_SIZE = 100
    universe = numpy.zeros((X_SIZE, Y_SIZE), dtype=bool)

    # start from (50,50)
    x = X_SIZE // 2
    y = Y_SIZE // 2
    x_dir = 0
    y_dir = 1
    up = True
    prev = False

    fig = plt.figure()
    plt.axis("off")
    frames = []

    for _ in range(11000):
        # animation
        frames.append((plt.imshow(universe, cmap='binary'),))

        # colour change
        old = universe[x][y]
        universe[x][y] = not old
        if old != up:
            # turn left
            was_x = x_dir
            x_dir = -y_dir
            y_dir = was_x
        else:
            # turn right
            was_x = x_dir
            x_dir = y_dir
            y_dir = -was_x
        
        # turn over if the colour of the square changed (!= means xor)
        up = up != old != prev
        prev = old

        # step
        x = (x + x_dir) % X_SIZE
        y = (y + y_dir) % Y_SIZE


    animation.ArtistAnimation(fig, frames, interval=25, blit=True,
                                repeat_delay=1000)
    #a.save("langton.html")

    plt.show()

if __name__ == '__main__':
    evolve()
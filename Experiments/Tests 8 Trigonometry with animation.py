import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

x = np.linspace(0, 2 * np.pi, 100)
line1, = ax1.plot(x, np.sin(x), 'r')
line2, = ax1.plot(x, np.cos(x), 'b')


def update(frame):
    line1.set_ydata(np.sin(x * frame / 10))
    line2.set_ydata(np.cos(x * frame / 10))
    return line1, line2


ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=50, blit=True)
plt.show()

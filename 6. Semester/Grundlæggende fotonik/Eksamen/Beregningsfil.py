import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots()
ax.grid()
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y = (np.tanh(x))**2
ax.plot(x, y)

# Set ticks in terms of π
xticks = np.arange(-3 * np.pi, 3.25 * np.pi, np.pi)
xtick_labels = [r"-$3\pi$", r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$"]
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels)
plt.show()



xtick_labels = [
    r"$0$" if i == 0 else 
    rf"$-\frac{{{abs(i)}}}{{4}}\pi$" if i < 0 and abs(i) != 4 else
    rf"$-{int(abs(i)//4)}\pi$" if i < 0 else
    rf"$\frac{{{i}}}{{4}}\pi$" if i != 4 and i % 4 != 0 else
    rf"${int(i//4)}\pi$" for i in range(-4, 5)
    ]
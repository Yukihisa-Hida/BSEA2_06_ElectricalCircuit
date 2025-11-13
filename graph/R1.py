import matplotlib.pyplot as plt
# import matplotlib_fontja
# import pandas as pd
import numpy as np
import math

plt.rcParams["font.family"] = "MS Mincho"
plt.rcParams["font.size"] = 15

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["legend.fancybox"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["legend.edgecolor"] = "black"
plt.rcParams["legend.markerscale"] = 5
plt.rcParams["lines.linewidth"] = 1
plt.rcParams["lines.linestyle"] = ""
plt.rcParams["lines.marker"] = "."

fig = plt.figure(dpi=200)

x1 = 0
x2 = 400
y1 = -1.5
y2 = 0

plt.xlim(x1, x2)
plt.ylim(y1, y2)

x = np.array([0, 52, 104, 158, 212, 266, 320, 374])
y = np.array([0,-0.158068155,-0.308454014,-0.448632717,-0.624723976,-0.770852012,-0.925753972,-1.16879202])

plt.plot(x, y, markeredgecolor='black', marker='o', markersize=5, color='black')

plt.rcParams["lines.linestyle"] = "-"

slope, intercept = np.polyfit(x, y, 1)
xmin, xmax = plt.xlim()
x_fit = np.array([xmin, xmax])
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, marker='', color='black')
print(f'最小二乗法による直線 (LSM Line)\ny = {slope:.6f}x + {intercept:.6f}')
plt.text(200, -1.4, f'y = {slope:.6f}x + {intercept:.6f}', fontsize=12)

plt.xlabel(r"時間$t_i\ \mathrm{\mu s}$")
plt.ylabel(r"電圧比の対数$\ \log{V_i/V_1}$")

plt.tight_layout()

plt.show()
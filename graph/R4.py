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
x2 = 300
y1 = -3.5
y2 = 0

plt.xlim(x1, x2)
plt.ylim(y1, y2)

x = np.array([0,25,50,75,100,125,150,175,200,225,250])
y = np.array([0,-0.329181803,-0.622529613,-0.940983344,-1.228665417,-1.516347489,-1.84176989,-2.104134154,-2.460809098,-2.797281335,-3.020424886])

plt.plot(x, y, markeredgecolor='black', marker='o', markersize=5, color='black')

plt.rcParams["lines.linestyle"] = "-"

slope, intercept = np.polyfit(x, y, 1)
xmin, xmax = plt.xlim()
x_fit = np.array([xmin, xmax])
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, marker='', color='black')
print(f'最小二乗法による直線 (LSM Line)\ny = {slope:.6f}x + {intercept:.6f}')
plt.text(150, -3.2, f'y = {slope:.6f}x + {intercept:.6f}', fontsize=12)

plt.xlabel(r"時間$t_i\ \mathrm{\mu s}$")
plt.ylabel(r"電圧比の対数$\ \ln{V_i/V_1}$")

plt.tight_layout()

plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

plt.rcParams["figure.figsize"] = 8,6

# -------- FUNCTION ------- #
def f(x):
    return np.array([x, ((x**4)-3*(x**3)+(x*x))])

def df(x):
    return 4*(x**3)-9*(x*x)+2*x

# ------- FIND MINIMA USING GRADIENT descent --------- #

def gradient_descent():
    xlist = [-1]
    slope = df(xlist[0])
    alpha = 0.05
    for i in range(50):
        xlist.append(xlist[i] - alpha * df(xlist[i]))
    return xlist

# ---------- GRAPH ---------- #
def update(x1):

    x,y = f(x1)
    point.set_data(x,y)
    text.set_text("Value : %.2f" % x1)
    return point, text,





fig, ax = plt.subplots()
fig.suptitle('GRADIENT DESCENT', fontsize=14)
fig.canvas.set_window_title('github.com/iam-abbas')
ax.axis([-10,10,-10,10])
ax.set_aspect("equal")
ax.set_xlabel('x')
ax.set_ylabel('y')
point, = ax.plot(0,1, marker="o")
text = ax.text(-9,9,"")
a= []
b = []
x = -5
while x<=5:
    y=(x**4)-3*(x**3)+x*x
    a.append(x)
    b.append(y)
    x += 0.1

ax.plot(a,b)


ani = FuncAnimation(fig, update, interval=50, blit=True, repeat=False,
                        frames=np.linspace(-3, max(gradient_descent())))
itr = 0
for x in gradient_descent():
    itr += 1
    print("Iteration", itr, ":", x)
plt.show()

#zadanie nr 2 według listy z pdf

import matplotlib.pyplot as plt
import pylab as p

a = int(input("Podaj a ="))
x1 = p.arange(-10,0,0.5)
x2 = p.arange(0.1,10,0.5)
Y1 = x1/(-3) + a
Y2 = x2*x2/3

plt.plot(x1, Y1, color='blue',linewidth=1.0, linestyle='-')
plt.plot(x2, Y2, color='green',linewidth=1.0, linestyle='-')
plt.xlabel("oś x")
plt.ylabel("oś y")

plt.title("Wykresy funkcji")
plt.grid(True)


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.plot(x1, Y1, color="blue",linewidth=2.5, linestyle="-",label="x/(-3)+a")
plt.plot(x2, Y2, color="green",linewidth=2.5, linestyle="-",label="x^2/3")
plt.legend(loc='upper left')

plt.show()

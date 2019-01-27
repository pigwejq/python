#zadanie 1 według pdf

import matplotlib.pyplot as plt
import pylab as p

a = int(input("Podaj a ="))
b = int(input("Podaj b ="))
x = p.arange(-10,10,1.0)
y = a*x+b

plt.plot(x,y)
plt.title("Wykres funkcji linowej")

plt.grid(True)

if a > 0:
    plt.text(2,2,'Funkcja rosnaca')
elif a == 0:
    plt.text(2,2,'Funkcja stala')
else:
    plt.text(2,2,'Funkcja malejaca')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


plt.show()


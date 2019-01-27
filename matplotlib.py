import matplotlib.pyplot as plt
import pylab as p
import numpy as ny

a = int(input("Podaj a = "))
b = int(input("Podaj b = "))
c = int(input("Podaj c = "))

x = p.arrange(-20,20,0.5)
y = a*x**2+b*x+c
plt(x,y)

#Napisz program, który na podstawie danych pobranych od użytkownika, czyli
#długości boków, sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt
#prostokątny. Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i
#pole, w przeciwnym wypadku komunikat, że nie da się utworzyć trójkąta.

import math
a = int(input("Podaj a (najdłuższy odcinek!): "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if a+b > c and a+c > b and b+c > a:
    print("Z tych boków zbudujesz trójkąt")
    if ((c*c)+(b*b)) == (a*a):
       print("Trójkąt jest prostokątny")
    obwod = a+b+c
    pobwod = obwod/2
    print("Obwód trójkąta wynosi: ", obwod)
    pole = math.sqrt(pobwod*(pobwod - a)*(pobwod-b)*(pobwod-c))
    print("Pole trójkąta wynosi: ", pole)
else:
    print("Z tych boków nie zbudujesz trójkątka")

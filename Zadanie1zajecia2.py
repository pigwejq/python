#Napisz program, który wypisuje liczby od START do STOP w kroku zadanym przez
#użytkownika. Umożliw użytkownikowi wprowadzenie liczby początkowej, liczby
#końcowej i wielkości odstępu między kolejnymi liczbami.

start = int(input("Podaj liczbę startową: "))
stop = int(input("Podaj liczbę końcową: "))
skok = int(input("Podaj skok: "))
print(start," ")
while start <= stop:
    start += skok
    if start <= stop:
        print(start," ")

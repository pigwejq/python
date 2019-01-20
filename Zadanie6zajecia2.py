#Pobierz od użytkownika n liczb i zapisz je w liście. Wydrukuj:
#1. elementy listy i ich indeksy,
#2. elementy w odwrotnej kolejności,
#3. posortowane elementy.
#4. Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.
#5. Usuń z listy element o podanym indeksie.
#6. Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
#7. Wybierz z listy elementy od indeksu i do j.

x = 1
lista = []
ileliczb = int(input("Podaj ile liczb chcesz wpisać: "))
while(x < ileliczb+1):
    liczba = int(input("Podaj liczbę numer: "))
    lista.append(liczba)
    x += 1
x = 0
while(x < ileliczb):
    print(x, end=" ")
    print(lista[x])
    x += 1
x = -1
while(x != -ileliczb):
    print(lista[x], end=" ")
    x -= 1
print(lista.sort)
dousuniecia = int(input("Podaj liczbę do usunięcia z listy: "))
lista.remove(dousuniecia)
dousuniecia = int(input("Podaj index do usunięcia: "))
lista.clear(dousuniecia)
pierwsza = int(input("Podaj pierwszą liczbę zakresu: "))
druga = int(input("Podaj drugą liczbę zakresu: "))
print(lista[pierwsza, druga])

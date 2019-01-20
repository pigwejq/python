#Utwórz grę, w której komputer wybiera losowo słowo, które gracz musi
#odgadnąć. Komputer informuje gracza, ile liter znajduje się w wybranym
#słowie. Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera
#jest zawarta w tym słowie. Komputer może odpowiedzieć tylko „tak” lub „nie”.
#Potem gracz musi odgadnąć słowo.

import random
slowa = ("python", "gdansk", "dlaczego", "gdynia", "wsb")
word = random.choice(slowa)
licznik = 1
x = 0
sprawdz = 0
print("Słowo ma ma ", len(word), " liter(y).")
while licznik < 5:
    licznik+=1
    zapytaj = input("Podaj literę: ")
    while x < len(word):
        if(word[x] == zapytaj):
            print("Ta litera występuje w tym wyrazie")
            x = 999
            sprawdz = 1
        x+=1
    if sprawdz == 0:
        print("Ta litera nie występuje w tym wyrazie")
    else:
        sprawdz = 0
    x = 0
odpowiedz = input("Teraz zgadnij jaki to wyraz: ")
if odpowiedz == word:
    print("Gratulacje, zgadłeś!")
else:
    print("Niestety, pomyliłeś się!")

#Utwórz program, który wczytuje komunikat użytkownika, a następnie wypisuje go w
#odwrotnej kolejności.

komunikat = input("Podaj dowolny wyraz: ")
x = 0
while x < len(komunikat):
    print(komunikat[len(komunikat)-1-x], end="")
    x+=1

#Wydrukuj alfabet w formacie: AaBbCcDd….., a następnie w formacie:
#aAbBcCdD…..

import string

alfabetM = string.ascii_lowercase
alfabetW = string.ascii_uppercase
licznik = 0
while licznik < len(alfabetW):
    print(alfabetM[licznik], end="")
    print(alfabetW[licznik], end="")
    licznik+=1
licznik = 0
print("\nDruga runda")
while licznik < len(alfabetW):
    print(alfabetW[licznik], end="")
    print(alfabetM[licznik], end="")
    licznik+=1


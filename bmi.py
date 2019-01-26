a = float(input("Podaj swoją wagę (kg): "))
b = float(input("Podaj swój wzrost (m): "))
bmi = a/(b*b)

print("Twoje BMI wynosi: ", bmi)

if bmi < 18.5:
    print("Masz niedowagę")
elif bmi >= 18.5 and bmi < 25:
    print("Mieścisz się w normie")
elif bmi >= 25 and bmi < 30:
    print("Okres przed otyłością")
elif bmi >= 30 and bmi < 35:
    print("Otyłość I")
elif bmi >= 35 and bmi < 40:
    print("Otyłość II")
elif bmi >= 40:
    print("Otyłość III")

a = int(input("Wciśnij coś: "))

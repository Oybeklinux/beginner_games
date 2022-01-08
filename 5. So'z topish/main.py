import random
import os

sozlar = ['mashina', 'nok', 'olma', 'banan']
soz = random.choice(sozlar)
soz = soz.lower()
print(soz)
urinish = 5
kiritilgan_harflar = []
habar = ""
while True: # 4 , "f"
    os.system('cls')
    yashirin_soz = ""
    for h in soz:
        if h in kiritilgan_harflar:
            yashirin_soz += h
        else:
            yashirin_soz += "█"

    print(yashirin_soz)
    print(f"Urinishlar: {urinish}")
    print(habar)

    if urinish == 0:
        print("Siz yutqazdingiz")
        break
    elif "█" not in yashirin_soz:
        print("Siz g'olib bo'ldingiz")
        break
    harf = input("Harf kiriting: ").lower()

    if harf in kiritilgan_harflar:
        habar = f"Siz {harf} hafrini kiritib bo'lgansiz"
    elif harf in soz:
        habar = f"{harf} harfi so'zda bor"
        kiritilgan_harflar.append(harf)
    else:
        habar = f"{harf} harfi so'zda yo'q"
        urinish -= 1
input("Chiqish ucun Enter ni bosing")
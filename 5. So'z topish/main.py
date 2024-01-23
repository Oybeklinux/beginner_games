import random
import os
import platform

sozlar = [
    ("uy hayvoni", ('kuchuk', 'ot', "qo'y", 'sigir', "echki", "eshak", "mushuk", "tovuq", "xo'roz")),
    ("yovvoy hayvoni", ("she'r", "tulki", "bo'ri", "quyon", "kiyik", "ilon", "timsoh")),
    ("meva", ("olma", "nok", "anjir", "malina", "qulupnay", "banan", "kivi", "anor")),
    ("sabzavot", ("bodring", "sabzi", "pamildori", "turup", "kartoshka", "piyoz", "sholg'om", "lavlagi", "balg'ari", "qalampir"))
]
soz_turi = random.choice(sozlar)

soz = random.choice(soz_turi[1])
soz = soz.lower()
print(soz)
urinish = 5
kiritilgan_harflar = []
habar = ""
while True: # 4 , "f"
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')
    print("===== So'z topish o'yini =====")
    print(f"Katakcha ortida qanday {soz_turi[0]} yashiringan?\n")
    yashirin_soz = ""
    for h in soz:
        if h in kiritilgan_harflar:
            yashirin_soz += h
        else:
            yashirin_soz += "☐"

    print(yashirin_soz)
    print(f"Urinishlar: {urinish}")
    print(habar)

    if urinish == 0:
        print("Siz yutqazdingiz")
        break
    elif "☐" not in yashirin_soz:
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

input("\nChiqish ucun Enter ni bosing")
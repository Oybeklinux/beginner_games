import random
from os import system

sozlar = ["Ot", "mushuk", "qo'y", "echki", "fil"]
tasodifiy_soz = (random.choice(sozlar)).lower()
yashirin_soz = ""
rasmlar = ['', '██', '████', '██████', '████████', '██████████']
foy_harflar = []
jon = 5
# print(tasodifiy_soz)
habar = ""

sarlavha = "=== So'z o'yiniga hush kelibsiz ===\nHayvon nomini toping"
while True:
    # ekranni yangilab turish
    _ = system("cls")
    yashirin_soz = ""
    # yashirin so'zdan topilgan harfni ko'rsatish
    for harf in tasodifiy_soz:
        if harf not in foy_harflar:
            yashirin_soz += "_"
        else:
            yashirin_soz += harf.upper()
    # jonni belgilar bilan ko'rsatish va habarlarni chiqarish
    print(f"{sarlavha}\nJoningiz: {rasmlar[jon]}\n{habar}\n{yashirin_soz}")
    # Agar yashirin_soz da _ belgisi bo'lmasa hammasi topilgan bo'ladi
    if "_" not in yashirin_soz:
        print("Siz g'olib bo'ldingiz")
        break
    # Agar jon 0 bo'lsa, yutqazgan bo'ladi
    if jon == 0:
        print("Joningiz qolmadi. Yutqazdingiz")
        break
    foy_harf = input(f"\nHarf kiriting: ").lower()
    # harfni bor yo'qligiga tekshirish
    if foy_harf in foy_harflar:
        habar = "Bu harfni yozib bo'ldingiz"
    elif foy_harf in tasodifiy_soz:
        foy_harflar.append(foy_harf)
        habar = "To'g'ri"
    else:
        habar = "Xato"
        jon -= 1
input("\nChiqish uchun Enter ni bosing")
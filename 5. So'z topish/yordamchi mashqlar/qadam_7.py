import os
tasodifiy_soz = "MaShIna".lower()
urinish = 5
kiritilgan_hafrlar = []
yashirin_soz = ""
habar = ""
while True:
    os.system('cls')
    yashirin_soz = ""
    for harf in tasodifiy_soz:
        if harf not in kiritilgan_hafrlar:
            yashirin_soz += "█"
        else:
            yashirin_soz += harf
    print(f"So'z topish o'yini\n{yashirin_soz}\nUrinishlar: {urinish}\n{habar}")
    foyd_harf = input("Harf kiriting: ").lower()
    if foyd_harf in kiritilgan_hafrlar:
        habar = "Siz m hafrini kiritib bo'lgansiz"
    elif foyd_harf in tasodifiy_soz:
        habar = f"{foyd_harf} harfi so'zda bor"
        kiritilgan_hafrlar.append(foyd_harf)
    else:
        habar = f"{foyd_harf} harfi so'zda yo'q"

        urinish -= 1
    if urinish == 0:
        habar += "\nSiz yutqazdingiz"
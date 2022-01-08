tasodifiy_soz = "MaShIna".lower()
urinish = 5
kiritilgan_hafrlar = []

while True:
    print(f"Urinishlar: {urinish}")
    foyd_harf = input("Harf kiriting: ").lower()
    if foyd_harf in kiritilgan_hafrlar:
        print("Siz m hafrini kiritib bo'lgansiz")
    elif foyd_harf in tasodifiy_soz:
        print(f"{foyd_harf} harfi {tasodifiy_soz} so'zida bor")
        kiritilgan_hafrlar.append(foyd_harf)
    else:
        print(f"{foyd_harf} harfi {tasodifiy_soz} so'zida yo'q")

        urinish -= 1
    if urinish == 0:
        print("Siz yutqazdingiz")
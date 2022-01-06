print("=== Kalkulyator ===")
natija = 0
belgi = ""
for i in range(1000):
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    amal = int(input("Amalni tanlang:\n\t"
                     "1. Qo'shish\n\t"
                     "2. Ayirish\n\t"
                     "3. Ko'paytirish\n\t"
                     "4. Bo'lish\n"))
    if amal == 1:
        natija = a + b
        belgi = "+"
    elif amal == 2:
        natija = a - b
        belgi = "-"
    elif amal == 3:
        natija = a * b
        belgi = "*"
    elif amal == 4:
        natija = a // b
        belgi = "/"
    else:
        print("Bunday amal yo'q. Qayta kiriting.")
        continue
    print(f"{a} {belgi} {b} = {natija}")
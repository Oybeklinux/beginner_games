import random


def menu():
    birinchimi = True
    while True:
        if birinchimi:
            tanlov = input("""Qaysi darajani tanlaysiz?
                1. Oson
                2. O'rta
                3. Qiyin
                4. Chiqish
    (1-4) oraliqda son kiriting: """)
            birinchimi = False
        else:
            tanlov = input("Xato. (1-4) oraliqda son kiriting: ")
        if tanlov.isdigit() and int(tanlov) in range(1, 5):
            return int(tanlov)


def oyin(daraja):
    takrorlash = 5
    bal = 0
    for j in range(takrorlash):
        amal = random.choice(["+", "-", "*", "/"])
        masala = None
        javob = None
        for i in range(daraja + 1):
            a = random.randint(1, 10)
            if i == 0:
                masala = str(a)
                javob = a
            else:
                masala += f" {amal} {a}"
                if amal == "+":
                    javob += a
                elif amal == "-":
                    javob -= a
                elif amal == "*":
                    javob *= a
                elif amal == "/":
                    javob = round(javob / a, 2)
        natija = input(f"Masalani javobini yozing: {masala} = ")
        if float(natija) == javob:
            print("To'g'ri")
            bal += 1
        else:
            print(f"Xato. To'g'ri javob: {javob}")
    print(f"Siz {takrorlash} savoldan {bal} ta to'g'ri javob topdingiz")


if __name__ == "__main__":
    oyin(1)
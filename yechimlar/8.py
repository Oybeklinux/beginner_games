import random


def bosh_doska_hosil_qil():
    """
    3x3 o'lchamli ro'yxat hosil qiladi
    :param
        None - hech narsa qaytarmaydi
    :return
        list - Hosil bo'lgan ro'yxatni qaytaradi
    """
    return [[i + 3 * j for i in range(1, 4)] for j in range(3)]


def doskani_korsat():
    """
    Doskani ekranga chiqaradi
    :return
        None - hech narsa qaytarmaydi
    """
    print("+-------+-------+-------+")
    for i in range(len(doska)):
        print(f"|       |       |       |")
        print(f"|   {doska[i][0]}   |   {doska[i][1]}   |   {doska[i][2]}   |""")
        print(f"|       |       |       |""")
        print(f"+-------+-------+-------+""")
    print()


def foydalanuvchi_tanlasin():
    """
    Foydalanuvchidan raqamni so'rab doskani o'zgartiradi
    :return
        None - hech narsa qaytarmaydi
    """
    global doska
    while True:
        raqam = int(input("Sizni galingiz: "))
        for i in range(3):
            for j in range(3):
                if doska[i][j] == raqam:
                    doska[i][j] = "O"
                    doskani_korsat()
                    return
        else:
            print("Bu katakda raqam mavjud")


def bosh_maydonlar():
    """
    doskadagi bo'sh raqamlar ro'yxatini qaytaradi, ya'ni
    (0 va X bo'lmagan raqamlarni) qaytaradi
    :return
        list - raqamlardan iborat bir o'lchamli roy'xat
    """
    bosh_kataklar = []
    for i in range(3):
        for j in range(3):
            if doska[i][j] != "X" and doska[i][j] != "O":
                bosh_kataklar.append(doska[i][j])
    return bosh_kataklar


def golib_bormi(belgi):
    """
    G'olib borligini aniqlaydi
        blegi - X yoki 0. X - Kompyuter, 0 - foydalanuvchi
    :return
        bool - True agar g'olib mavjud bo'lsa, False g'olib bo'lmasa
    """

    for i in range(3):
        if doska[i][0] == doska[i][1] == doska[i][2] == belgi:
            return True
    for i in range(3):
        if doska[0][i] == doska[1][i] == doska[2][i] == belgi:
            return True
    return doska[0][0] == doska[1][1] == doska[2][2] == belgi or \
           doska[2][0] == doska[1][1] == doska[0][2] == belgi


def kompyuter_tanlasin():
    """
    Kompyuter qolgan raqamlar orasidan tasodifiy tanlab,
    usha raqam o'niga X belgisini qo'yadi
    :return
        None - hech narsa qaytarmaydi
    """
    global doska
    raqam = random.choice(bosh_maydonlar())

    for i in range(3):
        for j in range(3):
            if doska[i][j] == raqam:
                doska[i][j] = "X"
                doskani_korsat()
                return


doska = bosh_doska_hosil_qil()
doska[1][1] = 'X'
doskani_korsat()

while bosh_maydonlar():
    foydalanuvchi_tanlasin()
    kompyuter_tanlasin()
    if golib_bormi("X"):
        print("Kompyuter g'olib")
        break
    elif golib_bormi("O"):
        print("Siz g'olib")
        break
else:
    print("Durrang")

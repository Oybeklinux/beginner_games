import os
from matem import oyin, menu


if __name__ == "__main__":
    while True:
        os.system('cls')
        tanlov = menu()
        if tanlov == 1:
            oyin(daraja=1)
        elif tanlov == 2:
            oyin(daraja=2)
        elif tanlov == 3:
            oyin(daraja=3)
        elif tanlov == 4:
            print("Chiqish")
        if input("O'yinni davom ettirasizmi? Xa(h): ") != "h":
            break
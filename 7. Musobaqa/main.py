import os
import random

file_users = "users"
file_words = "words"


def register():
    file = None
    while True:
        login = input("Login kiriting: ")
        if os.path.exists(file_users):
            file = open(file_users)
            user_exist = False
            for user in file.readlines():
                if login.lower() == user.strip():
                    print("Bu login bazada bor. Boshqa login yozing: ")
                    user_exist = True
                    break
            if not user_exist:
                break
        else:
            break
    if file:
        file.close()
    file = open(file_users, 'a')
    file.write(f"{login}\n")
    return login


def login():
    if not os.path.exists(file_users):
        return None, "Hozircha hech kim ro'yxatdan o'tmadi. Avval ro'yxatdan o'ting"
    user_login = input("Kirish uchun loginni kiriting: ")
    file = open(file_users)
    for db_login in file.readlines():
        values = db_login.split(",")
        if user_login == values[0].strip():
            return user_login, None

    return None, f"{user_login} logini bazada mavjud emas. Avval ro'yxatdan o'ting"


def menu(habar: str, lst: list):
    birinchi = True
    while True:
        if birinchi:
            tanlov = input(habar)
            birinchi = False
        else:
            tanlov = input("Xato. Qayta tering: ")
        if tanlov.isdigit() and int(tanlov) in lst:
            return int(tanlov)


def sub_menu(user_login):
    habar = f"Hush kelibsiz {user_login}"
    while True:
        os.system("cls")
        print(habar)
        tanlov = menu("""Bittasini tanlang:
        1. O'yinni boshlash
        2. Natijalarni ko'rish
        3. Orqaga qaytish\n""", range(1, 4))
        if tanlov == 1:
            habar = play(user_login)
        elif tanlov == 2:
            habar = show_results()
        elif tanlov == 3:
            break


def show_results():
    if not os.path.exists(file_users):
        return "Natijalar mavjud emas"
    file = open(file_users)
    users = {}
    habar = "O'yin natijalari:\n"
    for user in file.readlines():
        values = user.split(",")
        if len(values) == 2:
            users[values[1].strip()] = values[0].strip()
        else:
            users[values[0].strip()] = 0

    index = 0
    for value, key in sorted(users.items(), reverse=True):
        index += 1
        habar += f"{index} {str(key).center(20)} {value.center(20)}\n"
    return habar


def play(user):
    file = open(file_words, 'rt')
    lines = file.readlines()
    file.close()
    length = len(lines)
    user_points = 0
    wrong_answers = 0
    max_wrong_answers = 3
    habar = ""
    while True:
        line = random.randint(1, length)
        glossary = lines[line-1].split(",")
        uz, en = glossary[1], glossary[0]
        answer = input(f"{uz.strip()} so'zni tarjimasini yozing: ")
        if answer == en:
            user_points += 10
        else:
            print(f"Xato. To'g'ri javob: {en}")
            wrong_answers += 1
        if wrong_answers == 3:
            habar = f"Xatolar soni: {max_wrong_answers}\nTo'g'ri javoblar soni: {user_points//10}"
            break
    return write_results(user_points, user, habar)


def write_results(point, user_login, habar):
    file = open(file_users, 'r')
    users = file.readlines()
    for i in range(len(users)):
        values = users[i].split(",")
        if values[0].strip() == user_login:
            if len(values) == 2 and int(values[1].strip()) < point:
                users[i] = f"{values[0].strip()},{point}\n"
                habar += "\nAvvalgi natijalaringizga nisbatan rekord o'rnatdingiz"
            elif len(values) == 1:
                users[i] = f"{values[0].strip()},{point}\n"
            break

    file.close()
    file = open(file_users, 'w')
    file.write(''.join(users))
    file.close()
    return habar


if __name__ == "__main__":
    habar = ""
    while True:
        os.system("cls")
        print(habar)
        tanlov = menu("""________ Learn English words ________ 
    1. O'yin natijalari
    2. Ro'yxatdan o'tish
    3. Kirish
    4. Chiqish\n""", range(1, 5))
        if tanlov == 1:
            habar = show_results()
        elif tanlov == 2:
            user_login = register()
            sub_menu(user_login)
        elif tanlov == 3:
            user_login, habar = login()
            if user_login:
                sub_menu(user_login)
        elif tanlov == 4:
            break

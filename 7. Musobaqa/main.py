import json
import os
from random import choice

user_file = "users.txt"
word_file = "words.txt"


def sort_by_point(user):
    return user['point']


def show_results():
    if not os.path.exists(user_file):
        print("Natijalar mavjud emas")
        return

    with open(user_file) as file:
        users:list = json.load(file)
    users.sort(key=sort_by_point, reverse=True)
    print("O'yin natijalari:")
    index = 0
    for user in users:
        index += 1
        print(f"{index}{user['login'].center(20)}{str(user['point']).center(20)}")


def play(login):
    with open(word_file, 'r') as file:
        words = file.readlines()
    asked_words = []
    wrong_answer = 0
    right_answer = 0
    while True:
        while True:
            word = choice(words)
            if word not in asked_words:
                break
        asked_words.append(word)
        uz, en = word.split(",")
        en = en.strip()
        user_en = input(f"{uz} so'zni tarjimasini yozing: ")
        if user_en == en:
            right_answer += 1
        else:
            wrong_answer += 1
            print(f"Xato. To'g'ri javob: {en}")
            if wrong_answer == 3:
                print(f"Xatolar soni: {wrong_answer}\nTo'g'ri javoblar soni: {right_answer}")
                break
    with open(user_file) as file:
        users = json.load(file)
    for i in range(len(users)):
        if users[i]['login'] == login:
            point = right_answer * 10
            if users[i]['point'] < point:
                users[i]['point'] = point
                with open(user_file, 'w') as file:
                    json.dump(users, file, indent=4)


def sub_menu(login):
    while True:
        habar = """Bittasini tanlang:
            1. O'yinni boshlash
            2. Natijalarni ko'rish
            3. Orqaga qaytish\n"""
        tanlov = menu(habar, range(1,4))
        if tanlov == 1:
            play(login)
        elif tanlov == 2:
            show_results()
        else:
            break


def register():
    if not os.path.exists(user_file):
        user = {
            'login': input("Login kiriting: "),
            'password': input("Parolni kiriting: "),
            'point': 0
        }
        users = [user]
        with open(user_file, 'w') as file:
            json.dump(users, file, indent=4)
    else:
        with open(user_file) as file:
            users = json.load(file)
        while True:
            user = {
                'login': input("Login kiriting: "),
                'point': 0
            }
            user_exist = False
            for user_ in users:
                if user_['login'] == user['login']:
                    print("Bu login bazada bor. Boshqa login yozing: ")
                    user_exist = True
                    break
            if not user_exist:
                user['password'] = input("Parolni kiriting: ")
                with open(user_file, 'w') as file:
                    json.dump(users, file, indent=4)
                break
    sub_menu(user['login'])


def login():
    login = input("Kirish uchun loginni kiriting: ")
    with open(user_file) as file:
        users = json.load(file)
    for user in users:
        if user['login'].lower() == login.lower():
            parol = input("Parol: ")
            if user['password'] == parol:
                sub_menu(login)
                return
            else:
                print("Parol xato yozildi")
                return
    print(f"{login} logini bazada mavjud emas. Avval ro'yxatdan o'ting")




def menu(habar, royxat):
    while True:
        tanlov = input(habar)
        if tanlov.isdigit() and int(tanlov) in royxat:
            return int(tanlov)


if __name__ == "__main__":
    while True:
        habar = """________ Learn English words ________ 
            1. O'yin natijalari
            2. Ro'yxatdan o'tish
            3. Kirish
            4. Chiqish\n"""
        tanlov = menu(habar, range(1, 5))
        print(tanlov)
        if tanlov == 1:
            show_results()
        elif tanlov == 2:
            register()
        elif tanlov == 3:
            login()
        else:
            break

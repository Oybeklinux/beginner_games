from random import choice

users = {"otabek": {"password": 123, "point": 0}, "anvar": {"password": 123, "point": 10}}
words = {
    "mosina": "car",
    "avtobus": "bus",
    "uy": "home",
    "maktab": "school",
    "kuchuk": "dog",
    "mushuk": "cat",
    "qo'y": "sheep",
    "ot": "horse",
    "ilon": "snake",
    "bormoq": "go",
    "kelmoq": "come",
    "yugurmoq": "run",
    "sakramoq": "jump",
    "o'qimoq": "read",
    "yozmoq": "write",
    "kitob": "book",
    "kompyuter": "computer",
    "dastur": "software",
    "choy": "tea",
    "suv": "water",
    "ota": "father",
    "ona": "mother",
    "aka": "brother",
    "opa": "sister",
    "qalam": "pencil",
    "ruchka": "pen",
    "stol": "table",
    "stul": "chair",
    "ko'cha": "street"
}


def sort_by_point(user):
    return users[user]["point"]


def show_results():
    names = sorted(users, key=sort_by_point, reverse=True)
    i = 0
    for name in names:
        i += 1
        print(f"{i}. {name.title()}    {users[name]['point']} bal")
    print()


def play(login):
    global users, words

    asked_words = []
    wrong_answer = 0
    right_answer = 0
    question_num = 5
    for i in range(question_num):
        uz, en = choice(list(words.items()))
        del words[uz]
        asked_words.append(en)
        user_en = input(f"{uz} so'zni tarjimasini yozing: ")
        if user_en == en:
            right_answer += 1
        else:
            wrong_answer += 1
            print(f"Xato. To'g'ri javob: {en}")
            if wrong_answer == 3:
                print(f"Xatolar soni: {wrong_answer}\nTo'g'ri javoblar soni: {right_answer}")
                break
    print(f"\nO'yin tugadi. {question_num} tadan {right_answer} ta to'g'ri topdingiz")
    point = right_answer * 10
    if point > users[login]["point"]:
        users[login]["point"] = point


def sub_menu(login):
    print(f"\n{login.title()}, o'yinga hush kelibsiz ")
    while True:
        habar = """Bittasini tanlang:
            1. O'yinni boshlash
            2. Natijalarni ko'rish
            3. Chiqish\n"""
        tanlov = menu(habar, range(1, 4))
        if tanlov == 1:
            play(login)
        elif tanlov == 2:
            show_results()
        else:
            break


def register():
    global users
    while True:
        login = input("Login kiriting: ")
        if not login:
            print("Login bo'sh bo'lmasligi kerak")
        elif login in users:
            print("Bu login bazada bor. Boshqa login yozing: ")
        else:
            break
    while True:
        password = input("Parolni kiriting: ")
        if not password:
            print("Parol bo'sh bo'lmasligi kerak")
        elif len(password) <= 3:
            print("Parol uzunligi 3 dan katta bo'lishi kerak")
        else:
            break
    users[login] = {
        'password': password,
        'point': 0
    }

    sub_menu(login)


def login():
    login = input("Kirish uchun loginni kiriting: ")
    password = input("Parolingiz: ")
    if login not in users or password != users[login]["password"]:
        print(f"Login yoki parol xato kiritildi")
        return

    sub_menu(login)


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

        if tanlov == 1:
            show_results()
        elif tanlov == 2:
            register()
        elif tanlov == 3:
            login()
        else:
            break

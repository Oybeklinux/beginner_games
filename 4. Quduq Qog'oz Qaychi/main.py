# Quduq, Qog'oz, Qaychi
# Qadam 1. Kompyuter Quduq, Qog'oz, Qaychi lardan birini tasodifiy ravishda tanlaydi
# Qadam 2. Foydalanuvchi Quduq, Qog'oz, Qaychi lardan birini kiritadi
# Qadam 3. Uch holatga tekshirish:
        # 1. Kompyuter yutishi,
        # 2. Foydalanuvchi yutadi
        # 3. Durrang
# Qadam 4. 10 marta takrorlansin
# Qadam 5. Hisob chiqarilsin:
            # (Kompyuter) x:y (Foydalanuvchi)
            # Durranglar soni: z

import random

print("!!! Quduq Qaychi Qog'oz o'yiniga hush kelibsiz !!!\n")
# Quduq <- Qaychi, Qaychi <- Qog'oz, Qog'oz <- Quduq Kompyuter
# Quduq -> Qaychi, Qaychi -> Qog'oz, Qog'oz -> Quduq Foydalanuvchi
# Quduq = Qaychi, Qaychi = Qog'oz, Qog'oz = Quduq    Durrang
variant = {1:"Quduq", 2: "Qaychi", 3: "Qog'oz"}
foy = 0
kom = 0
dur = 0
for i in range(10):
    k = random.choice(list(variant.keys()))
    f = int(input(f"Bittasini yozing: {variant}:\n"))
    if k == 1 and f == 2 or k == 2 and f == 3 or k == 3 and f == 1:
        print("Kompyuter yutdi")
        kom += 1
    elif k == f:
        print("Durrang")
        dur += 1
    else:
        print("Siz yutdingiz")
        foy += 1
    print(f"(Kompyuter) {variant.get(k)}:{variant.get(f)} (Foydalanuvchi)")
print(f"Hisob: (Kompyuter) {kom}:{foy} (Foydalanuvchi)\nDurranglar soni: {dur}")
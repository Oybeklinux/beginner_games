import random

ixtiyoriy = random.randint(1, 100)
counter = 0
for i in range(1_000_000):
    son = int(input("Sonnni kiriting: "))
    counter += 1
    if ixtiyoriy == son:
        print(f"Siz yutdingiz. Siz {counter} martada javobni topdingiz")
        break
    elif ixtiyoriy < son:
        print(f"Xato. Siz kiritgan son katta")
    else:
        print(f"Xato. Siz kiritgan son kichik")
input("\nChiqish uchun Enterni bosing")
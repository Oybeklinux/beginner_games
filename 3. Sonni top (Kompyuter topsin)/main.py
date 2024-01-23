import random

boshi = 1
ohiri = 100
counter = 0
for i in range(1_000_000):
    son = random.randint(boshi, ohiri)
    javob = input(f"{son} Son tengmi (t) Son kattami (k) Son kichikmi (c): ")
    counter += 1
    if javob == "t":
        print(f"Topdim. Urinishlar soni: {counter}")
        break
    elif javob == "k":
        ohiri = son - 1
    elif javob == "c":
        boshi = son + 1

input("\nChiqish uchun Enterni bosing")
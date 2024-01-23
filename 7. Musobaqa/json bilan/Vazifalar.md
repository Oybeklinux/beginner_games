 1. Quyidagi menyuni yasang
```text
________ Learn English words ________ 
    1. O'yin natijalari
    2. Ro'yxatdan o'tish
    3. Kirish
    4. Chiqish
```
2. pass kalit so'zi bilan funksiyalar strukturasini yozing: 
- show_results()
- register()
- login()

3. Menyuni cheksiz tsiklga oling. So'ng tanlovga mos funksiyalarni chaqiradigan qiling. Ya'ni agar foydalanuvchi 
- 1 ni tanlasa show_results()
- 2 ni tanlasa register()
- 3 ni tanlasa login()
- 4 ni tanlasa chiqib ketsin
 
4. register() funksiyasini yozamiz:
   1. Foydalanuvchidan login va parolni so'rab, uni json formatda faylga yozamiz
   2. Agar fayl bo'lsa, ketidan yozsin
   3. Agar faylda bunday login mavjud bo'lsa, qayta kiritsin
   
- Agar ro'yxatdan o'tmagan bo'lsa
```text
Login kiriting: oybek
Parolni kiriting: 123
Hush kelibsiz oybek
```
- Aks holda quyidagi habar chiqsin
```text
Login kiriting: oybek
Bu login bazada bor. Boshqa login yozing: 
Login kiriting: otabek
Parolni kiriting: 234
Hush kelibsiz otabek
Bittasini tanlang:
        1. O'yinni boshlash
        2. Natijalarni ko'rish
        3. Orqaga qaytish
```
5. login() funksiyasi.
   1. Foydalanuvchidan login so'rasin
   2. Fayldan hamma foydalanuvchilar ro'yxatini o'qib loginni solishtirsin, agar login bazada mavjud bo'lmasa, chiqib ketsin
   3. Agar login bazada bo'lsa, so'ng parolni so'rasin, parolni ham solishtirsin, agar teng bo'lsa, keyingi menyuni ochsin
     
- Agar ro'yxatdan o'tgan bo'lmasa
```text
Kirish uchun loginni kiriting: test
test logini bazada mavjud emas. Avval ro'yxatdan o'ting
________ Learn English words ________ 
    1. O'yin natijalari
    2. Ro'yxatdan o'tish
    3. Kirish
    4. Chiqish
```
- Agar ro'yxatdan o'tgan bo'lsa
```text
Kirish uchun loginni kiriting: oybek
parol: 123
Hush kelibsiz oybek
Bittasini tanlang:
        1. O'yinni boshlash
        2. Natijalarni ko'rish
        3. Orqaga qaytish
```
6. play() funksiyasini yozish:
- words.txt degan fayl yarating. So'ng quyidagi ko'rinishida so'zlarni saqlang:
```text
maktab,school
kuchuk,dog
mushuk,cat
```
- so'zlarni fayldan o'qib o'zbekcha inglizcha so'zlar ro'yxatni hosil qiling
- cheksiz tsiklda tasodifiy so'z tanlasin ekranga chiqarsin
- chiqarilgan so'z boshqa qaytarilmasin
- foydalnuvchidan tarjimasi so'ralsin, so'ng taqqoslasin, xato va to'g'ri javoblar hisoblansin
- 3 xatodan so'ng natijani e'lon qilib chiqib ketsin
- foydalanuvchi natijasi oldingi natijadan katta bo'lsa, yangilab qo'ysin
  - hamma foydalanuvchilarni fayldan o'qib olamiz
  - tsiklda foydalanuvchi logini yordamida usha foydalanuvchini topamiz
  - bali katta bo'lsa, o'zgartirib, yana yozish uchun fayl ochib yozib qo'yamiz
```text
yugurmoq so'zni tarjimasini yozing: runn
```
- foydalanuvchi kiritgan so'z to'g'ri bo'lsa, keyingi so'z chiqadi, agar xato bo'lsa, quyidagi habar chiqadi
```text
Xato. To'g'ri javob: run
```
- natijasni users faylida saqlab qo'ying
- xato qilsa, o'yin tugaydi, xato va to'g'ri javoblar ko'rsatiladi:
```text
Xatolar soni: 3
To'g'ri javoblar soni: 0
Bittasini tanlang:
        1. O'yinni boshlash
        2. Natijalarni ko'rish
        3. Orqaga qaytish
```
7. Natijalarni ko'rsatish (show_results) funksiyasini yozing. Bazani *users* deb nomlang:
- Agar foydalanuvchilar bazasi mavjud bo'lsa, ma'lumot quyidagi kamayish tartibida chiqsin
```text
O'yin natijalari:
1        Otabek                 40         
2        Oybek                  10
```
- Agar baza mavjud bo'lmasa quyidagi habar chiqsin
```text
Natijalar mavjud emas
```
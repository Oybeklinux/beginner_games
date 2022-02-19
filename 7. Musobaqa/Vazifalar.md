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
- sub_menu

3. Menyuni cheksiz tsiklga oling. So'ng tanlovga mos funksiyalarni chaqiradigan qiling. Ya'ni agar foydalanuvchi 
- 1 ni tanlasa show_results()
- 2 ni tanlasa register()
- 3 ni tanlasa login()
- 4 ni tanlasa chiqib ketsin

4. Natijalarni ko'rsatish (show_results) funksiyasini yozing. Bazani *users* deb nomlang:
- Baza ko'rinishi quyidagicha bo'ladi:
```text
oybek,20
otabek,10
```
- Agar baza mavjud bo'lsa va login bazada bo'lmasa, ma'lumot quyidagi jadval ko'rishinishida chiqsin
```text
O'yin natijalari:
1        Otabek                 40         
2        Oybek                  10
```
- Agar login bazada mavjud bo'lsa, qayta login kiritishni so'rasin:
```text
Login kiriting: oybek
Bu login bazada bor. Boshqa login yozing: 
Login kiriting:
```
- Agar baza mavjud bo'lmasa quyidagi habar chiqsin
```text
Natijalar mavjud emas
```
5. register() funksiyasini yozamiz:
```text
Login kiriting: oybek
Hush kelibsiz oybek
```
- Foydalanuvchi kiritgan loginni users nomli faylga yozib qo'ying
- Agar fayl bo'lmasa, yangi yaratib login qo'shish kerak
- Agar fayl bo'lsa, u holda avval usha foydalanuvchi borligini tekshirsin, agar bor bo'lsa tegishli habar chiqarsin va qayta login kiritishni so'rasin, toki faylda mavjud bo'lmagan loginni kiritguncha so'rayversin:
```text
Login kiriting: oybek
Bu login bazada bor. Boshqa login yozing: 
Login kiriting:
```
6. login() funksiyasi.
- Agar fayl mavjud bo'lmasa quyidagicha habar chiqsin
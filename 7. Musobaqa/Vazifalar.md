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
- Agar ro'yxatdan o'tmagan bo'lsa
```text
Login kiriting: oybek
Hush kelibsiz oybek
```
- Aks holda quyidagi habar chiqsin
```text
Login kiriting: oybek
Bu login bazada bor. Boshqa login yozing: 
Login kiriting: otabek
Hush kelibsiz otabek
```
6. login() funksiyasi.
- Agar ro'yxatdan o'tgan bo'lsa
```text
Kirish uchun loginni kiriting: ulugbek
ulugbek logini bazada mavjud emas. Avval ro'yxatdan o'ting
```

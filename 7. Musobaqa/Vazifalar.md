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

4. Natijalarni ko'rsatish (show_reaults) funksiyasini bajaring:
- Fayl yarating. Faylda login va balni yozing orasini biror belgi bilan ajrating
- open() bilan faylni ochib, tsiklda qatorma-qator o'qib, bal bo'yicha tartiblangan holda quyidagi ko'rinishda natijalarni ekranga chiqaring:
  - Buning uchun users nomli bo'sh lug'at yarating. Tsiklda har bir qatorni lug'atda qo'shing: dict{"login": bal}
  - So'ng sorted(users.items()) funksiyasi yordamida uni teskari tartiblan
  - Tartib raqamni generatsiya qiling
  - So'ng ekranga quyidagi formatda chiqaring
```text
O'yin natijalari:
1        Otabek                 40         
2        Oybek                  10
```
- Agar fayl bo'lmasa, quyidagicha habar chiqsin:
```text
Natijalar mavjud emas
```

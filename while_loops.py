# kullanım yapısı
# senaryo1
# while <şart doğruyken>:
#     <burada yazılanı yap>


x= 0

while x<10:
    print("{} degeri 10'dan küçüktür".format(x))
    x += 1

# kullanım yapısı
# senaryo2
# while <şart doğruyken>:
#     <burada yazılanı yap>
# else: 
#     <burada yazılanı yap>

y=0
while y<10:
    print("{} degeri 10'dan küçüktür".format(y))
    y += 1
else:
    print("{} degeri 10'dan küçük değil".format(y))

#faktöriyel
#sayi degerinden başlayıp azalarak 0 a kadar gidiyor çarpa çarpa
sayi = 6
sonuc = 1

while sayi>0:
    sonuc = sonuc*sayi
    sayi-= 1
print(sonuc)
# bilerek whie ın dışına yazdık her çarpımda yazmasın diye sadece sonucu aldık


# toplam sembolü
sayi3 = 5
sonuc2= 0
while sayi3 > 0:
    sonuc2 = sonuc2+sayi3
    sayi3 -= 1
print(sonuc2)
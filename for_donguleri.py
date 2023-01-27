# for döngüsü

# for <degisken> in <iterable>:
    #<burada yazılanı yap>


yorum_birakanlar = ['ilkay inan','burçin inan', 'zeynep demir','ece inan','ibrahim inan','mehmet çimen']
for kullanici in yorum_birakanlar:
    print(kullanici) 

kullanici_Sayisi = 0
for kullanici in yorum_birakanlar:
    kullanici_Sayisi = kullanici_Sayisi +1
    print(kullanici_Sayisi,kullanici)


kullanici_Sayisi = 0
ad, soyad = yorum_birakanlar[0].split()[0], yorum_birakanlar[0].split()[1]
print(ad)
print(soyad)

for kullanici in yorum_birakanlar:
    kullanici_Sayisi = kullanici_Sayisi +1
    ad,soyad = kullanici.split()[0],kullanici.split()[1]
    print ('{0}.Kullanicinin Adi {1} ve Soyadi {2}'.format(kullanici_Sayisi,ad,soyad))



moderator = 'ece inan'
kullanici_Syisi = 0
moderator_sayisi = 0
for kullanici in yorum_birakanlar:
    ad,soyad = kullanici.split()[0],kullanici.split()[1]

    if (kullanici == moderator):
        moderator_sayisi += 1
        print ('{0}.Moderatorün Adi {1} ve Soyadi {2}'.format(moderator_sayisi,ad,soyad))
    else:
        kullanici_Syisi += 1
        print ('{0}.Kullanicinin Adi {1} ve Soyadi {2}'.format(kullanici_Syisi,ad,soyad))
        
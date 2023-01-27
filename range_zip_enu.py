# range
# range(10)

print(list(range(10)))

print([*range(10)])   # daha teknik yazım tipi

print([*range(2,7,2)]) # 3. paramatre atlama elemanı

for sayi in range(10):
    if sayi >5:
        print(sayi+1)



# enumarate
harfler = ['a','b','c','d','e']
for index,harf in enumerate(harfler): # enumerate indexleri de getirir
    print("{}. harf:{}".format(index+1,harf)) 


#zip  listeleri birleştirmek için kullanılıyor
ulkeler = ['TR','FR','DE']
siralamalar = range(1,4)

for ulke in zip(ulkeler,siralamalar):
    print(ulke)

for ulke,siralama in zip(ulkeler,siralamalar):
    print(ulke)





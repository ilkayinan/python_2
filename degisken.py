#degirken tipleri
#tip          kısaltma      örnek
#integer      int           3 , 10
#float        float         3.0, 5.1
#string       str           "slm", 'ilkay'
#Boolean      bool          True, False
#list         list          [1,2,True,"a",1] aynı eleman birden fazla kez kullanılabilir
#set          set           {1,2,True} aynı eleman iki kez kullanılamaz
#Dictionary   dict          {'isim':'ilkay', 'yas':32} tek bir elemanın farklı özellikleri
#Tuple        tup           (1,2, True) tuple daki değerler değiştirilemez

#sayılar
#int: tam sayı
#float:ondalıklı sayı

print(3)
print(type(3))
print(type(1.5))
print(3+4)
print(5%3) #mod işareti işlem sonucunda kalanı döndürür.
#matematiksel işlemlerde standart öncelikli işlemleri önce yapar.
print(3.1*5)


#string

strvar = "Python"
print(strvar)
print(strvar[0])
print(strvar[-1])
print(strvar[0:2])
print(strvar[2:])
print(strvar[1::2])
print(strvar[:2])
print(len(strvar)) #uzunluk bulur

#ekleme
strvar= strvar + " ogren!"
print(strvar)

print(strvar*5)

print(strvar.upper()) # bütün harfleri büyütür
print(strvar.lower())
print(strvar.split('n'))
strvar.split()


#boolean
a = True
b = False
c = 'True'
print(a)
print(b)
print(type(c))
print(type(a))

yas1=20
yas2=18

print(yas1>18)
print(yas2>18)

print(yas2==18)
print(yas1==18) #eşit mi

print(yas2!=18) #eşit değil mi

print(not yas2>18) # not ne çıkıyorsa tam tersini döndürür büyük küçükte ! kullanılmaz

#koleksiyon veri tipleri (list[] ve set{})

# [a ,  b ,  c ,  d ,  e ,  a]
#  0 |  1 |  2 |  3 |  4 |  5 
#  0 | -5 | -4 | -3 | -2 | -1 

liste = ["a","b","c","d","e","a"]
print(liste)

liste = liste + ['f'] # listeye sadece liste eklenebilir
print(liste)

print(liste[0:3])

liste.append('g')  #listeye eleman ekler 
print(liste)

print(liste.pop()) # son elemanı listeden atar ve değişkeni dışarı atar
print(liste)

print(liste.pop(5)) 
print(liste)



sayilar=[123,45687,78954,23,2,35,1,1]
sayilar.sort()   # sort sıralama yapar tekrarlayan ifadeleri ellemez
print(sayilar)

sayilar.reverse()  #listeyi tersine çevirir
print(sayilar)


set(sayilar) # işe yaramıyor
print(sayilar)

sayilar2={2,9,3,6,5,3,2} # set aynı değerleri tutmaz bir tane saklar
print(sayilar2)


#Tuple  değiştirilemez

# [a ,  b ,  c ,  d ,  e ,  a]
#  0 |  1 |  2 |  3 |  4 |  5 
#  0 | -5 | -4 | -3 | -2 | -1 

liste2 = ['a','b','c','d','e','a']
print(liste)
tup = ('a','b','c','d','e','a')
print(tup)
liste2[0] = 12312
print(liste2)

x = tup.count('a') # a dan kaç tane var
y= tup.count('t')
print(x,y)

print(tup.index('b')) # indexini verir
print(tup.index('a')) # birden fazla varsa ilkini verir
# print(tup.index('x')) x içerde olmadığı için hata veriyor

# dictionary çok boyutlu veri tipi

dict1 = {'isim': 'ilkay', 'yas': 36, 'lokasyon':'izmir'}
print(dict1)

dict2 = {
    'isim': 'ilkay',
    'yas': 36,
    'dogdugu_sehir': 'izmir',
    'yasadıgı_sehir': 'istanbul'
}
print(dict2)

dict3 = {
    'isim': 'ilkay',
    'yas': 36,
    'lokasyon': {
        'dogdugu_sehir': 'istanbul',
        'yasadıgı_sehir': 'izmir'
    }
}
print(dict3)
print(dict2['yas'])
print(dict3['lokasyon']['dogdugu_sehir'])

print(dict2.get('yas')) 
print(dict3.get('lokasyon').get('yasadıgı_sehir'))
print(dict3.keys())  #keyleri getirir
print(dict2.values())  # keylere karşılık gelen değerleri getirir
print(dict2.items())  # key ve value leri tek tek getirir







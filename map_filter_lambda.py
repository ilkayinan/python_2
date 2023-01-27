#map, filter ve lambda

# map listenin her elemanına aynı operasyonu uygular

# filter listenin içinde şarta uygun değişkenleri seçer

def karesini_al(x):
    print(x**2)
    return x**2
karesini_al(12)

sayilar = [*range(1,6)]
print(sayilar)

for index in range(len(sayilar)):
    sayilar[index]=karesini_al(sayilar[index])
print(sayilar)

#map
sayilar1=[*range(1,6)]
[*map(karesini_al,sayilar1)]

# filter
def cift_sayilari_filtrele(x):
    if x%2==0:
        print(x)
        return x
    else :
        return None
    
cift_sayilari_filtrele(3)

def cift_sayilari_filtrele2(x):
    print (x if x%2==0 else None)
cift_sayilari_filtrele2(3)

sayilar3 = [*range(1,11)]
print([*filter (cift_sayilari_filtrele,sayilar3)])

print([*map(lambda sayi:sayi**2,sayilar3)])

print([*filter(lambda x:x if x%2==0 else None, sayilar3)])
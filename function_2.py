# fonksiyonların birbiri ile ilişkisi
def buyuk_sayiyi_dondur(a,b):
    if a>b:
        return a
    else:
        return b

def metin_yazdir(a,b):
    buyuk_sayi= buyuk_sayiyi_dondur(a,b)
    sablon_metin = "{} daha büyük sayidir".format(buyuk_sayi)
    print(sablon_metin)
metin_yazdir(5,10)


# birden fazla değişken döndürme

def isim_soyisim_ayirma(isim_soyisim):
    isim = isim_soyisim.split()[0]
    soyisim = isim_soyisim.split()[1]
    print('isim:{}, soyisim:{}'.format(isim,soyisim))
    return isim,soyisim
    

a,b= isim_soyisim_ayirma("ilkay inan")
print(a)

#args argümanı
def isim_soyisim_birlestir(isim,soyisim):
    print(" ".join([isim,soyisim])) 

isim_soyisim_birlestir('ilkay','inan')

def isim_soyisim_birlestir(*args):
    for item in args:
        print(item)
    print(" ".join(args))  

# kwargs  = key word arguman

def gobek_adi_yazdir(**kwargs):
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print("göbek adı yok.")

gobek_adi_yazdir(adi='ilkay',gobekadi='burçin',  soyadi='inan')

isim_soyisim_birlestir('ilkay','burçin','inan') 


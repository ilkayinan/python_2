# yapı
# def <fonksiyonismi>(<argümanlar>):
# """"
# kodun işi 
# ...  return/print

def bes_bastir():
    """
    kod ile ilgili açıklamaları buraya yaz
    """
    print(5)
bes_bastir()

# print/return farkı

def bes_dondur():
    return 5

a= bes_dondur()
b= bes_bastir()
print(a)
print(b)

# argümanlar

def sayi_dondur(sayi):
    return sayi

c=sayi_dondur(10)
print(c)


def sayi_dondur(sayi=250): # aksi iddaa edilmediği sürece default 250 alır
    return sayi

d=sayi_dondur()
print(d)


def buyuk_sayiyi_dondur(a,b):
    if a>b:
        print(a)
    else:
        print(b)
buyuk_sayiyi_dondur(3,2)






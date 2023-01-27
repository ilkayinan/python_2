girdi=input("Bir sayi girin:")
print(girdi)
print(type(int(girdi)))


def uygulama():
    girdi2=input("Bir sayi girin:")
    islem = input("sayı çift mi tek mi?:")
    if islem=='cift':
        if int(girdi2)%2 ==0:
            print('Evet {} sayısı bir çift sayıdır'.format(girdi2)) 
        else: 
            print('Hayır {} sayısı bir çift sayı değildir'.format(girdi2)) 
    elif islem =='tek':
        if int(girdi2)%2==1:
            print('Evet {} sayısı bir tek sayıdır'.format(girdi2))
        else:
            print('hayır {} sayısı bir tek sayı değildir '.format(girdi2))

uygulama()





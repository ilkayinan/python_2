def sayi_girdisi_kontrol():
    girdi = input("bir sayı giriniz:")

    if girdi.isdigit():
        print("tebrikler! sayı tipi değer girdiniz..")
    else:
        print("Üzgünüm! bu bir sayı tipi değişken değil..")

sayi_girdisi_kontrol()


def sayi_girdisi_kontrol_dongu():
    girdi = input("bir sayı giriniz")
    tekrar =1

    while not girdi.isdigit():
        if tekrar==3:
            pass
        else:
            print("Üzgünüm! bu bir sayı tipi değişken değil..")
            tekrar +=1
            girdi = input("bir sayı giriniz:")
    else: 
        print("tebrikler! sayı tipi değer girdiniz..")

sayi_girdisi_kontrol_dongu()
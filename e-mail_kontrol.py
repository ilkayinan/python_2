def eposta_kont():
    girdi = input("geçerli bir eposta adresi giriniz")
    while not (('.' in girdi) and ('@' in girdi)):
        print("üzgünüm geçerli bir e-posta adresi değil...")
        girdi = input("geçerli bir eposta adresi giriniz")

    else:
        print("tebrikler eposta adresiniz ile giriş yaptınız")

eposta_kont()
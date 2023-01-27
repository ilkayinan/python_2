#break
harfler = ['a','b','c','d','e']*100
for index,harf in enumerate(harfler):
    if harf == 'c':
        print('{} harfi {}. indexte!'.format(harf,index))
        break # ilk değişkeni bulduktan sonra döngüden çıkar



#continue
for sayi in range(1,6):
    if sayi%2==0: # çift sayı sorgulama
        continue # çift sayılara gelince hiçbir şey yapmadan devam eder
    print(sayi)


#pass

for sayi in range(1,6):
    if sayi%2==0: # çift sayı sorgulama
        pass # 
    else:
        print(sayi)

if sayi<5:
    pass
else:
    print('hey')
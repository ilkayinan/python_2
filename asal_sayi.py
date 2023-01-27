deger=40
x=deger-1

while x>1:
    if deger%x==0:
        print('{} saysısı asal değil'.format(deger))
        break
    else:
        x-=1
else:
    print('{} sayısı asaldır'.format(deger))
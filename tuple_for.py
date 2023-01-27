tup1 = (1,3,5,7)

for sayi in tup1:
    print(sayi)

liste =[[1,2,3],[3,4,5],['a','b','c']] #aşağıda aldığımız eleman sayısı ile iç listedeki eleman sayısı aynı olmalı

for sayi1,sayi2,sayi3 in liste:
    print(sayi1)


liste2 = [[2,4,6],[3,6,9],[4,5,6]]

for x,y,z in liste2:
    print(x,y)
    print(x*y)


kullanici1 = {
    'ad': 'ilkay',
    'soyad':'inan'
}
print(kullanici1.keys())
print(kullanici1.values())
print(kullanici1.items())
print(kullanici1)

for k, v in kullanici1.items():
    print("Key: {} \t Value:{}".format(k,v)) #\t tab demek düzgün gözüksün diye var

for k in kullanici1.keys():
    print("Key: {}".format(k))

for v in kullanici1.values():
    print("Value: {}".format(v))

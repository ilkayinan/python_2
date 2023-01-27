# if <koşul sağlanıyorsa>
   #<burada yazılanı yap>

hava_durumu = 'yagisli'
if hava_durumu == 'yagisli':
    print('Semsiyeni Al!')


# if <koşul sağlanıyorsa>
   #<burada yazılanı yap>
# else:
   #<burada yazılanı yap>

hava_durumu = 'karli'
if hava_durumu == 'yagisli':
    print('Semsiyeni Al!')
else:
    print('sorun yok')



# if <koşul sağlanıyorsa>
#   #<burada yazılanı yap>
#elif <alternatif kosul sağlanıyorsa>
    #<burada yazılanı yap>
# else:
    #<burada yazılanı yap>

hava_durumu = 'karli'
if hava_durumu == 'yagisli':
    print('Semsiyeni Al!')
elif hava_durumu == 'karli':
    print('atkını al')
else:
    print('sorun yok')



yas = 16

if yas > 14:
    print('selam')
else:
    print('yürü git')


liste = ['a','b','c']
print (liste)
hedef_harf = 'd'
if hedef_harf in liste:
    print('buldum')
else:
    liste.append(hedef_harf)
    print('mevcut değildi ama eklendi')
print (liste)

hedef_harf = 'e'
if hedef_harf in liste and hedef_harf == liste[0]:
    print('buldum ve ilk harf konumunda')
elif hedef_harf in liste:
    print('buldum')
else:
    liste.append(hedef_harf)
    print('mevcut değildi ama eklendi')

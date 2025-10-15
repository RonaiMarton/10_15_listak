honapok = ['január', 'február', 'március', 'április', 'május', 'junius', 'julis', 'augustus']

print(type(honapok))

#lista hossza
print(len(honapok))

#a 0. indexű első elem
print(honapok[0])

print(honapok[1])
print(honapok[2])

#hátulról az első, vagyis az utolsó elem
print(honapok[-1])

#az egyes és a kettes indexű elemek kiírása
print(honapok[1:3])

#az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

#a kettes indexű elemtől a végéig
print(honapok [2:])

# join(): a lista elemeit egy sztringgé fűzi össze
# a megadott elválasztó karakterekkel tagolva
print(', '.join(honapok))

#lista bejárása
for i in range(len(honapok)):
    print(honapok[i])

#lista bejárása for - items
print("HONAPOK")
for honap in honapok:
    print(honap)
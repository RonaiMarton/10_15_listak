honapok = ['január', 'február', 'március', 'április', 'május', 'junius', 'julis', 'augustus']
szamok = [1, 2, 4, 6, 75, 5]

sorted_honapok = sorted(honapok)
print(sorted_honapok)

reversed_sorted_szamok = sorted(szamok, reverse=True)
print(reversed_sorted_szamok)

#hanyas indexen van
print(szamok.index(4))

#benne van-e
print(4 in szamok)

#osszead ketto listat
osszefog = honapok.extend(szamok)
print(osszefog)
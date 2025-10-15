# honapok = ['január', 'február', 'március', 'április', 'május', 'junius', 'julis', 'augustus']

# #hozzá ad a lista végéhez egy elemet
# honapok.append('szeptember')
# print(honapok)

# #név szerint töröl
# honapok.remove('április')

# #index szerint töröl
# honapok.pop(1)

# print(honapok)


months = ['január', 'február', 'március', 'április', 'május', 'junius', 'julis', 'augustus']
months.append('szemptember')

months.pop()
print(months)

deleted_months = months.pop()
print(f"utolso honap: {deleted_months}")
print(months)

print(months.remove('február'))

print(months.clear())

months.insert(0, "február")
print(months)
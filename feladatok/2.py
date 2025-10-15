"""
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából,
majd írja ki a módosított listát a képernyőre!

"""
import random
number_list = []
for i in range(10):
    number = random.randint(1,3)
    number_list.append(number)
print(number_list)
ask_to_remove = int(input("enter a number from 1 to 3 to delete\n"))
for i in range(number_list.count(ask_to_remove)):
    number_list.remove(ask_to_remove)
print(number_list)
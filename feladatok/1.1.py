"""
A program tároljon egy listában színeket. 
Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. 
A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""

colors = ['red', 'blue', 'green', 'yellow']
ask_color = input("enter a color to know if it is in the list \n")
print(f"is it there: {ask_color in colors}, here is the full list: {colors}")
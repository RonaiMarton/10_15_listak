"""
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! 
Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""
colors = ['red', 'blue', 'green', 'yellow']
ask_color = input("enter a color to know how many times it is in the list \n")

if ask_color in colors:
    print(colors.count(ask_color))
else:
    print(f"{ask_color} isnt in the list, here is the full list: {colors}")
"""
1-100ig lista, egy amely csak 3mal, egy amely csak 5tel, egy amely mindkettovel osztahto
"""
three_list = []
five_list = []
both_list = []

for i in range(101):
    if i % 3 == 0:
        three_list.append(i)
    elif i % 5 == 0:
        five_list.append(i)
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        both_list.append(i)
        
print(f"list of numbers only devidable by 3: {three_list} \n list of numbers only devidable by 5: {five_list} \n list devidable by both 3 and 5: {both_list}")
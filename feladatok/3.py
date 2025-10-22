"""
Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!
"""
num_dev_three = []

for i in range(41):
    if i % 3 == 0:
        num_dev_three.append(i)
print(f"heres the numbers divedable by 3: {num_dev_three}")
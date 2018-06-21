"""
Your input will contain one or more lines, where each line will be in the form of "NdM"; for example:
3d6
4d12
1d10
5d4
You should output the sum of all the rolls of that specified die, 
each on their own line. so if your input is "3d6", the output should look something like
"""
import random

def dice_roller(dstring):
    num_dice, den_dice = dstring.split('d')

    total = 0
    for _ in range(int(num_dice)):
        total += random.randint(1,int(den_dice))

    return total


dice_in = input("Input dice: ")
print(dice_roller(dice_in))

""" Other solution:

from random import randint

def dice_roller(s):
    n, d = map(int, s.split('d'))
    res = [randint(1, d) for _ in range(n)]
    print('{}:'.format(sum(res)), *res)

inputs = '''5d12
6d4
1d2
1d8
3d6
4d20
100d100'''

for i in inputs.split('\n'):
    dice_roller(i)
"""

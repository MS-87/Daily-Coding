"""
In mathematics the regular paperfolding sequence, also known as the dragon curve sequence, 
is an infinite automatic sequence of 0s and 1s. At each stage an alternating sequence of 1s and 0s 
is inserted between the terms of the previous sequence. The first few generations of the sequence look like this:
1
1 1 0
1 1 0 1 1 0 0
1 1 0 1 1 0 0 1 1 1 0 0 1 0 0
Your challenge today is to implement a regular paperfold sequence generator up to 8 cycles (it gets lengthy quickly). 
"""


def paperfold(iterations, numlist = []):
    if not numlist:
        numlist = [1]

    templist = [1]
    appendint = 0
    for x in numlist:
        templist.append(x)
        templist.append(appendint)
        appendint = int(not(appendint))

    if iterations:
        numlist = paperfold(iterations-1, templist)

    return "".join(str(x) for x in numlist)

iterations = 8
print(paperfold(iterations))

'''
output:
1101100111001001110110001100100111011001110010001101
1000110010011101100111001001110110001100100011011001
1100100011011000110010011101100111001001110110001100
1001110110011100100011011000110010001101100111001001
1101100011001000110110011100100011011000110010011101
1001110010011101100011001001110110011100100011011000
1100100111011001110010011101100011001000110110011100
1000110110001100100011011001110010011101100011001001
1101100111001000110110001100100011011001110010011101
1000110010001101100111001000110110001100100
'''

'''
#Smarter guy solution:

arr = [1]
for i in range(8):
    arr = arr + [1] + [bit ^ 1 for bit in arr[::-1]]

print(''.join([str(bit) for bit in arr]))
'''
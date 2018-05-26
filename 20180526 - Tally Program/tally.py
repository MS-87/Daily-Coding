'''
5 Friends (let's call them a, b, c, d and e) are playing a game and need to keep track of the scores. 
Each time someone scores a point, the letter of his name is typed in lowercase. 
If someone loses a point, the letter of his name is typed in uppercase. 
Give the resulting score from highest to lowest.
'''

def score(tally):
    #accepts an input string. uses a dict to keep track of each score
    scoring = {}
    for x in tally:
        scoring[x.upper()] = 0

    for y in tally:
        if y.islower():
            scoring[y.upper()] = scoring[y.upper()] + 1
        else:
            scoring[y.upper()] = scoring[y.upper()] - 1

    print(scoring)


tal_in = input("Input tally string: ")
score(tal_in)

'''
test input/output:
abcde: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
dbbaCEDbdAacCEAadcB: {'D': 2, 'B': 2, 'A': 1, 'C': 0, 'E': -2}
EbAAdbBEaBaaBBdAccbeebaec: {'E': 1, 'B': 0, 'A': 1, 'D': 2, 'C': 3}
'''




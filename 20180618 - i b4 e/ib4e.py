"""
Write a function that tells you whether or not a given word follows the "I before E except after C" rule.
"""

import re
import urllib.request

def check(word):
    """returns true or false if it follows the rule"""


    ciePattern = re.compile(r'cie')
    eiPattern = re.compile(r'[^c]ei')
    
    result1 = re.search(ciePattern, word)
    result2 = re.search(eiPattern, word)

    if result1 or result2:
        return False
    return True

def iterate_all():
    """iterate all words on file. count number of exceptions"""
    all_words = urllib.request.urlopen("https://norvig.com/ngrams/enable1.txt")

    violations = 0
    for line in all_words:
        if not check(str(line)):
            violations += 1


    print(violations)



iterate_all()

"""
check("a") => true
check("zombie") => true
check("transceiver") => true
check("veil") => false
check("icier") => false

Challenge 1 Ouptput:
>2169

"""


""" Different solution

### Challenge Solution
def check(_word: str) -> bool:
    if "ei" in _word.replace("cei",""): return False
    if "cie" in _word: return False
    return True

while True:
    print(check(input()))
### Bonus (run `wget "https://norvig.com/ngrams/enable1.txt" -O words.txt` to download words list).
with open('words.txt','r') as f:
    words = [word.strip() for word in f.readlines()]

false = 0

for word in words:
    false = false + 0 if check(word) else false +1

print(false)


=========OR==========


import re

def check(word):
    return not re.search(r'cie|(?<!c)ei', word)
"""
import random
from random import randrange
import time

f = open("4digit.txt","w+") 
pin1 = str(randrange(0,9))
pin2 = str(randrange(0,9))
pin3 = str(randrange(0,9))
pin4 = str(randrange(0,9))
f.write(pin1+pin2+pin3+pin4)
f.close()

with open("4digit.txt") as file:
    file_contents = file.read()
    print(file_contents)
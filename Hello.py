import random
from random import randint
print("hi")
luck = random.randint(1, 3)
print(luck)
loto = (int(input("Pick a number from 1 to 3: ")))
while luck != loto:
    if loto > 0 and loto < 4:
        print("closey")
        loto = (int(input("Pick a number from 1 to 3: ")))
    elif loto <= 0 or loto > 3:
        print("Not closey")
        loto = (int(input("NOOOOOPick a number from 1 to 3: ")))
else:
    for i in range(8):
        print("WIN" * 10)


import random
from random import randint

print("To win pick a number between 1 to 3 in less than 2 guesses")
luck = random.randint(1, 3)
print("The answer will be " + str(luck))
loto = (int(input("Pick a number from 1 to 3: ")))
counter = 0

while luck != loto:

    if 0 < loto < 4:
        counter += 1
        print("closey")
        print(counter)
        if counter > 1:
            print("too many guesses")
            break
        loto = (int(input("Pick a number from 1 to 3 in less than 2 guesses: ")))
    elif loto <= 0 or loto > 3:
        print("Not closey")
        loto = (int(input("NOOOOO Pick a number from 1 to 3: ")))


else:
    for i in range(8):
        print("WIN" * 10)

import random

dobbelsteen = [1, 2, 3, 4, 5, 6]


def monopolyworp():
    dubbel = 0

    while True:
        worp1 = random.choice(dobbelsteen)
        worp2 = random.choice(dobbelsteen)
        totaal = worp1 + worp2
        print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(totaal))
        if worp1 == worp2:
            dubbel += 1
            if dubbel == 3:
                print('Je moet naar de gevangenis')
                break
        else:
            break


monopolyworp()

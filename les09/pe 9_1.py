try:
    bedrag = 4356
    aantal = int(input('Aantal personen: '))
    if aantal < 0:
        raise ArithmeticError
    print('Prijs per persoon is: {} euro'.format(bedrag / aantal))
except ZeroDivisionError:
    print('Delen door 0 is niet toegestaan!')
except ValueError:
    print('Het aantal personen moet in cijfers (0-9) worden aangegeven!')
except ArithmeticError:
    print('Het aantal personen kan niet negatief zijn!')
except SyntaxError:
    print('Oeps. Er is iets mis gegaan!')

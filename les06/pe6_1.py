def seizoen(maand):
    if 2 < maand < 6:
        return 'lente'
    elif 5 < maand < 9:
        return 'zomer'
    elif 8 < maand < 12:
        return 'herfst'
    elif maand == 12 or maand == 1 or maand == 2:
        return 'winter'
    else:
        return 'maand niet bekend'

maand1 = int(input('Geef maand nummer: '))
print(seizoen(maand1))

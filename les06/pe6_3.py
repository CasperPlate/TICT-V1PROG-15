invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
string = invoer.split('-')
getallen = []
for i in string:
    getallen.append(int(i))

getallen.sort()

grootste = max(getallen)
kleinste = min(getallen)
aantal = len(getallen)
som = sum(getallen)
gemiddelde = som / aantal

print('Gesoorteerde list van ints:  {}'.format(getallen))
print('Grootste getal: {} en Kleinste getal: {}'.format(grootste, kleinste))
print('Aantal getallen: {} en Som van de getallen: {}'.format(aantal, som))
print('Gemiddelde: {}'.format(gemiddelde))


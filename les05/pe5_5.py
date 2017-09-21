zin = input('Geef mij eens een mooie zin: ')
woorden = zin.split()
totaal = 0
aantal = 0

for woord in woorden:
    aantal = aantal + 1
    totaal = totaal + len(woord)

gemiddelde = totaal / aantal
print('De gemiddelde lengte van alle woorden is: {:5.1f}'.format(gemiddelde))

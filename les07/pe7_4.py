def ticker(bestand):
    tickers = []
    with open(bestand, 'r') as bestaand:
        inhoud = bestaand.readlines()
        for regel in inhoud:
            tickers.append(regel.rstrip('\n').split(':'))
        return tickers


def ticker_finder(filename, waarde):
    gegevens = ticker(filename)
    for i in range(len(gegevens)):
        if gegevens[i][0] == waarde:
            return 'De ticker is: {}'.format(gegevens[i][1])
        elif gegevens[i][1] == waarde:
            return 'Het bedrijf is: {}'.format(gegevens[i][0])
    return 'Er is geen match gevonden'


print(ticker_finder('ticker.txt', input('Geef een ticker of bedrijf: ')))

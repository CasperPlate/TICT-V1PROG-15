leeftijd = eval(input('Geef je leeftijd: '))
paspoort = input('Nederlands paspoort (ja/nee): ')

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
elif leeftijd < 18 and paspoort == 'ja':
    print('Je moet nog even wachten voordat je mag stemmen.')
else:
    print('Je bezit niet het juiste paspoort om te stemmen.')

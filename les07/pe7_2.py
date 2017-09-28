while True:
    woord = input('Geef een string van vier letters: ')
    if len(woord) != 4:
        print('{} heeft {} letters'.format(woord, len(woord)))
    else:
        print('Dank je wel! {} heeft {} letters'.format(woord, len(woord)))
    if woord == 'stop':
        print('We gaan nu stoppen')
        break

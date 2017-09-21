infile = open('kaartnummers.txt', 'r')
content = infile.readlines()
infile.close()
nummers = []
namen = []
i = 0

for regel in content:
    kaartGegevens = regel.rstrip('\n').split(',')
    nummers.append(kaartGegevens[0])
    namen.append(kaartGegevens[1])

    print(namen[i] + ' heeft kaartnummer: ' + nummers[i])
    i = i + 1


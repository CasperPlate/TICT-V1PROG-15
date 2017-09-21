kaartnummers = open('kaartnummers.txt', 'r')
content = kaartnummers.readlines()
kaartnummers.close()
nummers = []
namen = []
i = 0

outfile = open('kaartnummersuit.txt', 'w')

for regel in content:
    kaartGegevens = regel.rstrip('\n').split(',')
    nummers.append(kaartGegevens[0])
    namen.append(kaartGegevens[1])

    outfile.write('{} heeft kaartnummer: {}\n'.format(namen[i], nummers[i]))
    i = i + 1
outfile.close()

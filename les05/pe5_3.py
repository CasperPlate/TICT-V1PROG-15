infile = open('kaartnummers.txt', 'r')
content = infile.readlines()
infile.close()

aantal = len(content)
nummers = []

for regel in content:
    gegevens = regel.rstrip('\n').split(',')
    nummers.append(gegevens[0])


hoogste = max(nummers)
regel = nummers.index(hoogste) + 1
print('Deze file telt ' + str(aantal) + ' regels')
print('Het grootste kaarnummer is: {} en dat staat op regel {}'.format(hoogste, regel))

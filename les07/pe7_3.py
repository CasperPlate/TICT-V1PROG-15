cursus = {'jan': 4, 'jaap': 5, 'johan': 8, 'jasper': 9.9, 'andre': 9.3, 'dirk': 7.2, 'truus': 6.5, 'rik': 5.6}

for naam in cursus:
    if cursus[naam] > 9:
        print('{} heeft een {}'.format(naam, cursus[naam]))

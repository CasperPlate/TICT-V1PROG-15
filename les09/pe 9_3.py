import csv

with open('users.csv', 'r') as Gamers_file:
    reader = csv.reader(Gamers_file, delimiter=';')
    hoogste_score = 0
    for rij in reader:
        if int(hoogste_score) < int(rij[2]):
            hoogste_score = rij[2]
            naam = rij[0]
            datum = rij[1]
    print('De hoogste score is: {} op {} behaald door {}'.format(hoogste_score, naam, datum))
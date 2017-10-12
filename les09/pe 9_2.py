import time
import csv

with open('inloggers.csv', 'w') as inloggers:

    writer = csv.writer(inloggers, delimiter=';')
    writer.writerow(('lokale tijd', 'achternaam', 'voorletters', 'geboortedatum', 'email'))

    while 1:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum (dd-mm-yyyy)? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((time.strftime('%a %d %B %Y at %H:%M', time.localtime()), voorl, naam, gbdatum, email))

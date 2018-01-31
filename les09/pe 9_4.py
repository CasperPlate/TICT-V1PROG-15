import csv

with open('winkelmandje.csv', 'w', newline='') as csv_kantoor_artikelen:
    csv_writer = csv.writer(csv_kantoor_artikelen, delimiter=';')
    csv_writer.writerow(('artikelnummers', 'artikelcode', 'product', 'aantal', 'prijs'))

    while True:
        artikelnummer = input("Wat is het artikelnummer? ")
        artikelcode = input("Wat is de artikelcode? ")
        product = input("Wat is je product van het product? ")
        aantal = input("Wat is het aantal van het product? ")
        prijs = input('Wat is de prijs van het product? ')
        doorgaan = input('Wil je nog een invoer doen? ')
        csv_writer.writerow((artikelnummer, artikelcode, product, aantal, prijs))

        if doorgaan in 'NeeneeNEE':
            break

with open('kantoor_artikelen.csv', 'r') as csv_kantoor_artikelen:
        csv_reader = csv.reader(csv_kantoor_artikelen, delimiter=';')
        header = next(csv_reader)
        duurste_artikel = 0
        totale_aantal = 0
        kleinste_vooraad = 1000
        for prijs in csv_reader:
            if float(duurste_artikel) < float(prijs[-1]):
                duurste_artikel = prijs[-1]
                product_product = prijs[2]

            if int(kleinste_vooraad) > int(prijs[-2]):
                kleinste_vooraad = prijs[-2]
                artikel_nummer = prijs[0]

            totale_aantal = totale_aantal + int(prijs[3])

print('Het duurste artikel is {} en die kost {} Euro'.format(product_product, duurste_artikel))
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(kleinste_vooraad, artikel_nummer))
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totale_aantal))
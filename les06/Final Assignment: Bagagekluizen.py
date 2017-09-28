status = 0


def keuzes():
    print('1: Ik wil weten hoeveel kluizen er nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    print('4: Ik geef mijn kluis terug')
    print('5: Ik ben klaar')


def keuze():
    status = eval('input("Geef uw keuze: ")')

    try:
        if 1 > int(status) > 5:
            print('Ongeldige keuze')
            status = 0
    except ValueError:
        print('Ongeldige keuze')
        status = 0
    return int(status)


def toon_aantal_kluizen_vrij():
    totaal = 12

    kluizen = open('kluizen.txt')
    inhoud = kluizen.readlines()
    kluizen.close()

    print('Aantal kluizen beschikbaar is: ' + str(totaal - len(inhoud)))


def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    kluizen = open('kluizen.txt', 'r')
    inhoud = kluizen.readlines()
    kluizen.close()

    for regels in inhoud:
        regel = regels.rstrip('\n').split(';')
        if int(regel[0]) in kluisnummers:
            kluisnummers.remove(int(regel[0]))

    if len(kluisnummers) > 0:
        wachtwoord = input('Geef een code (minimaal 4 karakters): ')
        if len(wachtwoord) >= 4:
            kluizen = open('kluizen.txt', 'a')
            kluizen.write('{};{}\n'.format(kluisnummers[0], wachtwoord))
            kluizen.close()
            print('U heeft kluisnummer: {} gekregen'.format(kluisnummers[0]))
        else:
            print('Het opgegeven wachtwoord is te kort, probeer opnieuw...')
    else:
        print('Er zijn geen kluizen meer beschikbaar')


def kluis_openen():
    kluizen = open('kluizen.txt', 'r')
    lines = kluizen.readlines()
    kluizen.close()
    kn = input('Geef uw kluisnummer: ')
    ww = input('Geef uw code: ')
    correct = False

    for line in lines:
        regel = line.rstrip('\n').split(';')
        if kn == regel[0] and ww == regel[1]:
            print('Uw kluis wordt geopend')
            correct = True

    if not correct:
        print('Uw kluisnummer en code komen niet overeen!')


def kluis_teruggeven():
    kn = input('Geef uw kluisnummer: ')
    ww = input('Geef uw code: ')

    with open('kluizen.txt', 'r') as rf:
        with open('kluizen_copy.txt', 'w') as wf:
            for line in rf:
                if line != '{};{}\n'.format(int(kn), ww):
                    wf.write(line)

    with open('kluizen.txt', 'w') as wf:
        with open('kluizen_copy.txt', 'r') as rf:
            for line in rf:
                wf.write(line)

    print('Bedankt voor het teruggeven van uw kluisje.')


while status != 5:
    status = 0
    keuzes()
    status = keuze()

    if status == 0:
        print('Kies nog een keer: ')

    elif status == 1:
        toon_aantal_kluizen_vrij()

    elif status == 2:
        nieuwe_kluis()

    elif status == 3:
        kluis_openen()

    elif status == 4:
        kluis_teruggeven()

    elif status == 5:
        print('Bedankt voor uw bezoek')



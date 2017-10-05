stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']


def inlezen_beginstation(station_lijst):
    while 1:
        station = input('Geef uw beginstation op: ')
        if station in station_lijst:
            return station
        else:
            print('Station behoort niet tot dit traject.')


def inlezen_eindstation(station_lijst, begin_station):
    while 1:
        station = input('Geef uw eindstation op: ')
        if station in station_lijst:
            if station_lijst.index(station) > station_lijst.index(begin_station):
                return station
            else:
                print('De trein is al langs het station geweest.')
        else:
            print('Station behoort niet tot dit traject.')


def omroepen_reis(lijst_stations, begin, eind):
    rang_begin = lijst_stations.index(begin) + 1
    rang_eind = lijst_stations.index(eind) + 1
    afstand = rang_eind - rang_begin
    print('Uw reisgegevens: ')
    print('Het beginstation is {} en dit is het {}e station, het eindstation is {} en dit is het {}e station.'.format(begin, rang_begin, eind, rang_eind))
    print('De afstand van de reis bedraagt {} station(s)'.format(afstand))
    print('De prijs van het kaartje is {} euro'.format(afstand * 5))
    print('Jij stapt in de trein in: {}'.format(begin))
    if afstand > 1:
        for i in range(rang_begin, rang_eind - 1):
            print('  -  {}'.format(lijst_stations[i]))
    print('Jij stapt uit de trein in: {}'.format(eind))


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

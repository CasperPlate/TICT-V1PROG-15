stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']


def inlezen_beginstation(begin_station):
    station = ''
    while station not in begin_station:
        station = input('Geef uw beginstation op: ')
        if station in begin_station:
            return station


def inlezen_eindstation(eind_station, begin_station):
    #work in progress

def omroepen_reis(lijst, begin, eind):
    #work in progress

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)


print(inlezen_beginstation(stations))

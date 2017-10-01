groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', "Helmond 't Hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}

print(groen.intersection(bruin))
print(bruin - groen)
print(bruin.union(groen))

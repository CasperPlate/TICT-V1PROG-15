cijferICOR = 10
cijferPROG = 10
cijferCSN = 10
gemiddelde = float((cijferICOR + cijferPROG + cijferCSN) / 3)
beloning = float(cijferICOR * 30 + cijferPROG * 30 + cijferCSN * 30)
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)


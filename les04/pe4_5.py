def kwadraten_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            som = som + (getal ** 2)
    return som

getallen = [4, 5, 3, -81]
print(kwadraten_som(getallen))

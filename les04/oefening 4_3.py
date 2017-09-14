getallen = eval(input('Geef een paar getallen: '))

def swap (lijst):
    if len(lijst) > 1:
        lijst[0], lijst[1] = lijst[1], lijst[0]
    return lijst

swap(getallen)
print(getallen)

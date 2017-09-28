getal = 1
getallenlijst = []
while getal != 0:
    getal = eval(input('Geef een getal: '))
    getallenlijst.append(getal)
print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallenlijst), sum(getallenlijst)))

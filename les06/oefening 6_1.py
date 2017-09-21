gewicht = eval(input('Wat is uw gewicht(kg): '))
lengte = eval(input('Wat is uw lengte(m): '))
BMI = gewicht / (lengte ** 2)

if BMI <= 18.5:
    print('ondergewicht')

elif 18.5 < BMI <= 25:
    print('normaal')
else:
    print('overgewicht')

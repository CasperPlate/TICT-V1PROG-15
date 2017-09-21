def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def table():
    print('  F      C')
    formatStr = '{0:5}  {1:5}'
    for i in range(-30, 41, 10):
        print(formatStr.format(convert(i), float(i)))

table()
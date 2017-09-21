strings = eval(input('Geef een lijst met minimaal 10 strings: '))
vierLetters = []

for i in range(len(strings)):
    if len(strings[i]) == 4:
        vierLetters.append(strings[i])

print('De nieuw-gemaakte lijst met alle vier-letter strings is: ')
print(vierLetters)

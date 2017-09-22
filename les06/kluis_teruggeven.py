kn = input('Geef uw kluisnummer: ')
ww = input('Geef uw code: ')

with open('kluizen.txt', 'r') as rf:
    with open('kluizen_copy.txt', 'w') as wf:
        for line in rf:
            if line != '{};{}\n'.format(int(kn), ww):
                wf.write(line)
with open('kluizen.txt', 'w') as wf:
    with open('kluizen_copy.txt', 'r') as rf:
        for line in rf:
            wf.write(line)

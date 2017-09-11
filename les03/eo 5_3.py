woord = input('Geef een woord: ');
E = 0;
O = 0;
I = 0;

for i in woord:
    if i == 'e':
        E+=1;
    if i == 'o':
        O+=1;
    if i == 'i':
        I+=1;

if E != 0:
    print('Het woord bevat ' + str(E) + ' keer de letter e.')
if O != 0:
    print('Het woord bevat ' + str(O) + ' keer de letter 0.')
if I != 0:
    print('Het woord bevat ' + str(I) + ' keer de letter i.')

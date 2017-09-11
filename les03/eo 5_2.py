getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
oneven = 0;
deelbaar = 0;

for i in getallenrij:
    if i%2 == 1:
        oneven+=1;
    if i+2 == 0 and i%3 == 0:
        deelbaar+=1;
print('Het aantal oneven getallen is: ' + str(oneven));
print('Het aantal getallen deelbaar door 2 en 3 is: ' + str(deelbaar));
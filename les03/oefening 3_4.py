getallenlijst = [2, 4, 6, 8, 10, 9, 7]

aantal = 0
for i in getallenlijst:
    if i%3 == 0:
        aantal+=1
print('Het aantal getallen deelbaar door 3 is: ' + str(aantal))

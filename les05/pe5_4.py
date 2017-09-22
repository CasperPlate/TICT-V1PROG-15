import time

try:
    hardlopers = open('hardlopers.txt', 'a')

except FileNotFoundError:
    hardlopers = open('hardlopers.txt', 'w')

i = 0
while i < 5:
    hardlopers.write(time.strftime('%a %d %b %Y, %H:%M:%S, ', time.localtime()) + input('Geef naam: ') + '\n')
    i = i + 1
hardlopers.close()

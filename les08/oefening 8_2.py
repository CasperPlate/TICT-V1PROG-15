set3 = set()
set7 = set()
set_alle = set()

for i in range(1, 999):
    if i % 3 == 0:
        set3.add(i)
    if i % 7 == 0:
        set7.add(i)
    set_alle.add(i)

print(set3)
print(set7)
print(set3 & set7)
print(set3 | set7)
print(set3 - set7)
print(set_alle - set7 - set3)


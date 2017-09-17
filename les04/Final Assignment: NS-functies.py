def standaardprijs(afstandKM):
    prijs = 0
    if afstandKM < 0:
        prijs = 0
        return prijs
    if afstandKM >= 0 and afstandKM <= 50:
        prijs = afstandKM * 0.8
        return prijs
    if afstandKM > 50:
        prijs = afstandKM * 0.6 + 15
        return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    ritprijs = 0
    ritprijs = standaardprijs(afstandKM)
    if (leeftijd < 12 or leeftijd > 64) and weekendrit == 0:
        ritprijs = ritprijs / 100 * 70
        return ritprijs
    if (leeftijd < 12 or leeftijd > 64) and weekendrit == 1:
        ritprijs = ritprijs / 100 * 65
        return ritprijs
    if (leeftijd > 11 and leeftijd < 65) and weekendrit == 0:
        return ritprijs
    if (leeftijd > 11 and leeftijd < 65) and weekendrit == 1:
        ritprijs = ritprijs / 100 * 60
        return ritprijs


# 11 en doordeweeks 50km
print('11 en doordeweeks standaard 50km ' + str(standaardprijs(50)))
print('11 en doordeweeks ritprijs 50km' + str(ritprijs(11, False, 50)))

# 11 en doordeweeks 60km
print('11 en doordeweeks standaard 60km ' + str(standaardprijs(60)))
print('11 en doordeweeks ritprijs 60km ' + str(ritprijs(11, False, 60)))

# 11 en weekend 50km
print('11 en weekend standaard 50km ' + str(standaardprijs(50)))
print('11 en weekend ritprijs 50km ' + str(ritprijs(11, True, 50)))

# 11 en weekend 51km
print('11 en weekend standaard 60km ' + str(standaardprijs(60)))
print('11 en weekend ritprijs 60km ' + str(ritprijs(11, True, 60)))

# 12 en doordeweeks 50km
print('12 en doordeweeks standaard 50km ' + str(standaardprijs(50)))
print('12 en doordeweeks ritprijs 50km ' + str(ritprijs(12, False, 50)))

# 12 en doordeweeks 60km
print('12 en doordeweeks standaard 60km ' + str(standaardprijs(60)))
print('12 en doordeweeks ritprijs 60km ' + str(ritprijs(12, False, 60)))

# 12 en weekend 50km
print('12 en weekend standaard 50km ' + str(standaardprijs(50)))
print('12 en weekend ritprijs 50km ' + str(ritprijs(12, True, 50)))

# 12 en weekend 60km
print('12 en weekend standaard 60km ' + str(standaardprijs(60)))
print('12 en weekend ritprijs 60km ' + str(ritprijs(12, True, 60)))

# 64 en doordeweeks 50km
print('64 en doordeweeks standaard 50km ' + str(standaardprijs(50)))
print('64 en doordeweeks ritprijs 50km ' + str(ritprijs(64, False, 50)))

# 64 en doordeweeks 60km
print('64 en doordeweeks standaard 60km ' + str(standaardprijs(60)))
print('64 en doordeweeks ritprijs 60km ' + str(ritprijs(64, False, 60)))

# 64 en weekend 50km
print('64 en weekend standaard 50km ' + str(standaardprijs(50)))
print('64 en weekend ritprijs 50km ' + str(ritprijs(64, True, 50)))

# 64 en weekend 60km
print('64 en weekend standaard 60km ' + str(standaardprijs(60)))
print('64 en weekend ritprijs 60km ' + str(ritprijs(64, True, 60)))

# 65 en doordeweeks 50km
print('65 en doordeweeks standaard 50km ' + str(standaardprijs(50)))
print('65 en doordeweeks ritprijs 50km ' + str(ritprijs(65, False, 50)))

# 65 en doordeweeks 60km
print('65 en doordeweeks standaard 60km ' + str(standaardprijs(60)))
print('65 en doordeweeks ritprijs 60km ' + str(ritprijs(65, False, 60)))

# 65 en weekend 50km
print('65 en weekend standaard 50km ' + str(standaardprijs(50)))
print('65 en weekend ritprijs 50km ' + str(ritprijs(65, True, 50)))

# 65 en weekend 60km
print('65 en weekend standaard 60km ' + str(standaardprijs(60)))
print('65 en weekend ritprijs 60km ' + str(ritprijs(65, True, 60)))

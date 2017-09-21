studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(cijfers):
    per_student = []
    for i in range(len(cijfers)):
        for j in range(len(cijfers[i])):
            som = sum(cijfers[i])
            lengte = len(cijfers[i])
            gemiddelde = som / lengte
        per_student.append(gemiddelde)
    return per_student


def gemiddelde_van_alle_studenten(cijfers):
    alle_studenten = 0
    som = sum(cijfers)
    lengte = len(cijfers)
    alle_studenten = som / lengte
    return alle_studenten


print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(gemiddelde_per_student(studentencijfers)))

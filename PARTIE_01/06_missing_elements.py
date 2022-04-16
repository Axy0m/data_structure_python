# ELEMENTS MANQUANTS DANS UNE LISTE entre 1 et 10 inclus

a = [3, 8, 2, 4, 7]


# METHODE 1

def get_missing_numbers(l, min, max):
    missing = []
    for i in range(min, max + 1):  # le max est toujours exclus du range donc +1 pour l'inclure
        if i not in l:
            missing.append(i)
    return missing


print(get_missing_numbers(a, 1, 10))


# *******************************
# METHODE 2 - COMPREHENSION DE LISTE

def get_missing_numbers2(l, min, max):
    return [i for i in range(min, max + 1) if i not in l]


print(get_missing_numbers2(a, 1, 10))

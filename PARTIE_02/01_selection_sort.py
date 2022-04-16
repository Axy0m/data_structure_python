import random

# TRI PAR SELECTION

""" PRINCIPE :

 On repére le plus petit élèment, on le sort de la liste pour le placer au début et ainsi de suite

 peu efficace avec beaucoup d'élèments - complexité de n² """


def generate_random_list(n, min, max):
    """
    FONCTION QUI GENERE UNE LISTE ALEATOIRE
    :param n:
    :param min:
    :param max:
    :return:
    """
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l


def selection_sort(l):
    for unsorted_index in range(0, len(l) - 1):
        min = l[unsorted_index]
        min_index = unsorted_index

        for i in range(unsorted_index + 1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i

        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min


l = generate_random_list(15, -1000, 1000)
print("UNSORTED: ", l)
selection_sort(l)

print("SORTED: ", l)

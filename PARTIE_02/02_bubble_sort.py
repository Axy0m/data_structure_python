import random

# TRI à BULLES

""" PRINCIPE :

On compare toujours 2 élèments successifs et s'assurer que l'élèment de gauche est le plus petit
en faisant des PERMUTATIONS

peu efficace avec beaucoup d'élèments - complexité de n² """

# l = [4, 8, 7, 2]
#
# [4, 7, 2, 8]   2 permutations
# [4, 2, 7, 8]   1 permutation
# [2, 4, 7, 8]   0 permutation => FIN


def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l


def bubble_sort(l):
    nb_permut = 1    # artificiel, c'est juste pour initialiser et entrer dans la boucle
    while nb_permut != 0:
        nb_permut = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:   # si élèment courant est > à l'élèment d'après
                nb_permut += 1
                a = l[i]        # on se rappelle de la valeur
                l[i] = l[i+1]   # on permute les 2 élèments
                l[i+1] = a      #


l = generate_random_list(10, 0, 10)
print("UNSORTED: ", l)

bubble_sort(l)
print("SORTED:   ", l)



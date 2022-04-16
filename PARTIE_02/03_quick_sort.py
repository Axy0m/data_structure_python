import random

# TRI RAPIDE

""" PRINCIPE :

On choisit au hasard un élèment qu'on appelle le PIVOT, et à partir de lui on va faire un 1er tri grossier:
les élèments plus grand que lui on les met à droite et les plus petits à gauche.

ex: arr = [8, 3, 7, 9, 1, 4] - p = 4
.... 4 .... le 4 est à sa place
* petits élèments : 3, 1
* grands élèments : 8, 7, 9

l'idée est de subdiviser qui permet de faire des opérations sur des longueurs de données plus petites
donc un algorithme moins gourmand en ressource

efficace - complexité de n log n """


def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l


def quick_sort(l):
    qsort_loop(l, 0, len(l) - 1)


def qsort_loop(l, imin, imax):
    # préconditions
    if imax - imin == 1:
        if l[imin] > l[imax]:
            l[imin], l[imax] = l[imax], l[imin]
        return
    if imax - imin == 0:
        return

    # choix du pivot
    p = l[imax]
    a = 0
    for i in range(imin, imax):
        if l[i] <= p:
            l[a + imin], l[i] = l[i], l[a + imin]
            a += 1
    l[a + imin], l[imax] = p, l[a + imin]
    if a != 0:
        qsort_loop(l, imin, a + imin - 1)
    if imax > a + imin + 1:
        qsort_loop(l, a + imin + 1, imax)


# fonction qui vérifie que la liste est bien ordonnée
def check_ordered(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True


l = generate_random_list(10, 0, 100)
print("UNSORTED: ", l)
quick_sort(l)
print("SORTED: ", l)

if check_ordered(l):
    print("VERIFIED")
else:
    print("ALGORITHM FAILED")

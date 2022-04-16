s = "Hello There !"


# METHODE 1 - BOUCLE FOR

def count_upper_characters1(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count


print(count_upper_characters1(s))


# ***********************************
# METHODE 2 - COMPREHENSION DE LISTE

def count_upper_characters2(s):
    l = [1 for c in s if c.isupper()]  # condition : la liste prend uniquement la valeur 1 si la lettre est une majuscule
    return len(l)


# lorque la condition est à droite, cela conditionne le fait que l'on mette l'élèment ou non dans la liste
# PAR CONTRE, lorsqu'elle est à gauche, cela va conditionner la valeur de l'élèment, donc obligé de donner une valeur et
# de faire un if else :
# l = [1 if c.isupper() else 0 for c in s]
# total = sum(l)


print(count_upper_characters2(s))

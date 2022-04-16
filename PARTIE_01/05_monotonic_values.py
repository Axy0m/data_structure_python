# ENSEMBLE DE DONNESS QUI S'INCREMENTE ou S'EGALISE TOUJOURS DANS LE MEME SENS

# METHODE 1

def is_increasing_monotonic_values1(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True


a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]

print("a:", is_increasing_monotonic_values1(a))
print("b:", is_increasing_monotonic_values1(b))


# ****************************
# METHODE 2 - TRI de la LISTE

def is_increasing_monotonic_values2(l):
    return l == sorted(l)  # si la liste est égale à sa version triée


a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]

print("a:", is_increasing_monotonic_values2(a))
print("b:", is_increasing_monotonic_values2(b))


# *******************************
# DECREASING

def is_decreasing1(l):
    for i in range(len(l) - 1):
        if l[i + 1] > l[i]:
            return False
    return True


a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]

print("a:", is_decreasing1(a))
print("b:", is_decreasing1(b))


# ****************************
# METHODE 2 - TRI de la LISTE

def is_decreasing2(l):
    return l == sorted(l, reverse=True)  # si la liste est égale à sa version triée


a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]

print("a:", is_decreasing2(a))
print("b:", is_decreasing2(b))

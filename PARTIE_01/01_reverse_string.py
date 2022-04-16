s = "Hello There !"

# ************************
# METHODE 1 - BOUCLE FOR


def reverse_string1(str):
    r = ""
    for c in str:
        r = c + r
    return r


print(reverse_string1(s))


# ************************
# METHODE 2 - SLICE

def reverse_string2(str):
    return s[::-1]


print(reverse_string2(s))

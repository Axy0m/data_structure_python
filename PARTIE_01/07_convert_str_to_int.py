chaine = "-1234"


# METHODE 1

def convert_str_to_int(c):
    # ord("4") - ord("0") FONCTION ord() donne la valeur du caractère ASCII
    #        4
    #   3 x 10
    #  2 x 100
    # 1 x 1000
    is_negative = c[0] == "-"

    string_to_convert = c
    if is_negative:
        string_to_convert = c[1:]

    # facteur multiplicateur f
    f = 1
    nb = 0
    for i in range(len(string_to_convert) - 1, -1, -1):
        n = ord(string_to_convert[i]) - ord("0")
        if n < 0 or n > 9:
            raise ValueError("Cette fonction ne peut convertir que des chiffres")
        nb += n * f
        f *= 10
    if is_negative:
        return -nb
    return nb


print(convert_str_to_int(chaine))

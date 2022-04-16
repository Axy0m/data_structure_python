# MOTS COMMUNS ENTRE 2 PHRASES


# METHODE 1
def get_common_words(a, b):
    words_a = a.lower().replace(",", "").split(" ")
    words_b = b.lower().replace(",", "").split(" ")

    common_words = []  # liste qui contient les résultats

    for word in words_a:
        # on regarde si ce mot existe dans b et ne se répète pas
        if word in words_b and not word in common_words:
            common_words.append(word)  # on l'ajoute dans la liste

    return common_words


a = "Bonjour bonjour je m'appelle Youyou"
b = "Bonjour, je suis Youn"

print(get_common_words(a, b))


# ************************************
# METHODE 2 - SET INTERSECTION()

def get_common_words2(a, b):
    words_a = set(a.lower().replace(",", "").split(" "))
    words_b = set(b.lower().replace(",", "").split(" "))

    # return list(words_a.intersection(words_b))
    # AUTRE ANNOTATION
    return list(words_a & words_b)


a = "Bonjour bonjour je m'appelle Youyou"
b = "Bonjour, je suis Youn"

print(get_common_words2(a, b))

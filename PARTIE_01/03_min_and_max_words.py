s = "Un chasseur sachant chasser sait chasser sans son chien"


# METHODE 1 - ordre dans la phrase

def get_min_and_max_words(sentence):
    words = sentence.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)

    return (min_word, max_word)


min_word, max_word = get_min_and_max_words(s)

print("Mot le plus petit :", min_word)
print("Mot le plus long :", max_word)


# **********************************************
# # METHODE 2 - par ordre alphabétique

def get_min_and_max_words_sorted1(sentence):
    words = sentence.split(" ")
    min_word, max_word = get_min_and_max_words(sentence)

    all_min_words = [w for w in words if len(w) == len(min_word)]
    all_max_words = [w for w in words if len(w) == len(max_word)]

    all_min_words.sort()
    all_max_words.sort()

    return all_min_words[0], all_max_words[0]


min_word, max_word = get_min_and_max_words(s)

print("Mot le plus petit :", min_word)
print("Mot le plus long :", max_word)


# # ****************************************
# # METHODE 3 -

def get_min_and_max_words_sorted2(sentence):
    words = sentence.split(" ")
    words.sort()
    min_word = min(words, key=len)
    max_word = max(words, key=len)
    return min_word, max_word


min_word, max_word = get_min_and_max_words_sorted2(s)

print("Mot le plus petit: ", min_word)
print("Mot le plus long: ", max_word)

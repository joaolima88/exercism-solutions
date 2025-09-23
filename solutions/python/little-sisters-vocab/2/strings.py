"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    
    return 'un' + word
    


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    lista_1 = vocab_words[1:] # This will just be a list of strings instead of a nested list.
    lista_2 =[]

    for word in lista_1: # Now word is each element of lista_2, which is a str
      lista_2.append(vocab_words[0] + word)
    
    lista_2.insert(0, vocab_words[0])
    return ' :: '.join(lista_2)
    
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    word_s = word[:-4]
    if word_s[-1] == 'i':
        return word_s[:-1] + 'y'
    else:
        return word_s
        

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    alpha_r = sentence[0:-1]
    lista = alpha_r.split(" ")
    return lista[index] + "en"  


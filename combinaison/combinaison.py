terms = {}


class Term:
    """
    Chaque char. du str correspond à un "Term"
    """
    def __init__(self, position, word, all_terms):
        """

        :param position: Position du char dans le mot
        :param word: Mot...
        :param all_terms: Liste des Term du mot
        """
        self.letter = word[position]
        self.position = position
        self.word = word
        self.terms = all_terms

    def set_possibilities(self):
        """
        liste les termes suivant autorisés
        Les termes autorisés sont ceux présents dans
        word2 et ceux qui sont présent apres l'index
        de la premiere occurence du terme actuel dans word2
        Initialise ensuite la liste des possibilites
        :return:
        """
        result = []
        for next_index in range(self.position + 1, len(self.word)):
            for possibility in self.terms[next_index].possibilties:
                result.append(self.letter + possibility)
        result.append(self.letter)
        self.possibilties = result


def get_possibilities(word):
    """
    :param word: str dont on veut les poss.
    :return: la liste des substr d'un mot
    """
    possibilities = []

    for k in reversed(range(len(word))):
        term = Term(k, word, terms)
        terms[k] = term
        term.set_possibilities()
        for b in terms[k].possibilties:
            possibilities.append(b)
    return possibilities


if __name__ == '__main__':
    import time
    a = time.time()
    get_possibilities("azertyuiopqsdfghjklm")
    print(time.time() - a)

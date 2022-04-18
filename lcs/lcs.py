terms = {}


class Term:
    """
    Chaque char. du str correspond à un "Term"
    """
    def __init__(self, position, word, allow, all_terms, word2):
        """

        :param position: Position du char dans le mot
        :param word: Mot...
        :param allow: Liste des index qu'on s'autorise à utiliser
        :param all_terms: Liste des Term du mot
        :param word2: Mot avec lequel la comparaison se fait
        """
        self.letter = word[position]
        self.position = position
        self.word = word
        self.allow = allow
        self.terms = all_terms
        self.word2 = word2

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
            next_letter = self.word[next_index]
            if next_index in self.allow and next_letter in self.word2[self.word2.index(self.letter)+1:]:
                for possibility in self.terms[next_index].possibilties:
                    result.append(self.letter + possibility)
        result.append(self.letter)
        self.possibilties = result


def get_possibilities(word, allow, word2):
    """
    :param word: str dont on veut les poss.
    :param allow: liste d'index autorisés
    :param word2:
    :return: la liste des substr d'un mot
    """
    possibilities = []

    for k in reversed(allow):
        term = Term(k, word, allow, terms, word2)
        terms[k] = term
        term.set_possibilities()
        for b in terms[k].possibilties:
            possibilities.append(b)
    return possibilities


def lcs(word1, word2):

    # Recupere dans l'ordre les lettres communes dans chaque mot
    allow_1 = [i for i in range(len(word1)) if word1[i] in word2]
    allow_2 = [i for i in range(len(word2)) if word2[i] in word1]

    p_1 = get_possibilities(word1, allow_1, word2)
    terms.clear()
    p_2 = get_possibilities(word2, allow_2, word1)

    # Tri en ordre inverse pour recuperer la plus longue chaine
    p_2.sort(key=len, reverse=True)
    p_1.sort(key=len, reverse=True)
    for element in p_1:
        for item in p_2:
            if element == item:
                return element


if __name__ == '__main__':
    import time
    a = time.time()
    print("Reponse :", lcs("aazertyuiodfvfdcfdvpp", "aazertyuiopp"))
    print(time.time() - a)

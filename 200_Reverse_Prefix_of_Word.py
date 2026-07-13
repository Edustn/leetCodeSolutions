class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: 
            return word

        pilha = []
        resultado = []
        for i, char in enumerate(word):
            pilha.append(char)

            if char == ch:
                while pilha:
                    resultado.append(pilha.pop())
                resto = word[i+ 1:]

                return "".join(resultado) + resto

        # lista1 = "".join(reversed(word[:word.index(ch)+1]))
        # lista2 = word[word.index(ch)+1:]

        # return f"{lista1}{lista2}"
            
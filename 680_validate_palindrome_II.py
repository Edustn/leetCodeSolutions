class Solution:

    def validPalindrome(self, s: str) -> bool:
        def ehPalindromo(esq, dir):
            while esq < dir:
                if s[esq] != s[dir]:
                    return False
                esq += 1 
                dir -= 1
            return True
        sChar = list(s)
        i = 0 
        j = len(s)-1

        while i < j:
            if s[i] != s[j]:
                return ehPalindromo(i + 1, j) or ehPalindromo(i, j - 1)
            i += 1
            j -= 1
        return True
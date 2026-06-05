class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        while i < j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                auxI = chars[i]
                chars[i] = chars[j]
                chars[j] = auxI
                i += 1
                j -= 1
            elif s[i].lower() in vowels and s[j].lower() not in vowels:
                j -= 1
            else:
                i += 1
        return "".join(chars)



            

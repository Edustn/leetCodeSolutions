class Solution:
    def reverseWords(self, s: str) -> str:
        phrase = s.split(' ')

        for i in range(len(phrase)):
            phrase[i] = phrase[i][::-1]

        return " ".join(phrase)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        childGreed = 0
        cookieSize = 0
        g = sorted(g)
        s = sorted(s)
        while childGreed < len(g) and cookieSize < len(s):
            if g[childGreed] <= s[cookieSize]:
                childGreed += 1
            cookieSize += 1
        return childGreed
        

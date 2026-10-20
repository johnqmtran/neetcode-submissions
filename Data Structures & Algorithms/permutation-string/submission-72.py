class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}

        for c in s1:
            counts1[c] = 1 + counts1.get(c, 0)
        
        need = len(counts1)
        for i in range(len(s2)):
            cur = 0
            counts2 = {}
            for j in range(i, len(s2)):
                counts2[s2[j]] = 1 + counts2.get(s2[j], 0)
                if counts1.get(s2[j], 0) < counts2[s2[j]]:
                    break
                if counts1.get(s2[j], 0) == counts2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False

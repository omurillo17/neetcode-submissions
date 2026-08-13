class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vistos1 = {}
        vistos2 = {}

        for i in s:
            if i in vistos1:
                vistos1[i] += 1
            else:
                vistos1[i] = 1

        for j in t:
            if j in vistos2:
                vistos2[j] += 1
            else:
                vistos2[j] = 1

        if vistos1 == vistos2:
            return True
        return False
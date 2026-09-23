class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ndict1 = {}
        ndict2 = {}

        for i in s:
            if i in ndict1:
                ndict1[i] += 1
            else:
                ndict1[i] = 1

        for j in t:
            if j in ndict2:
                ndict2[j] += 1
            else:
                ndict2[j] = 1

        return ndict1 == ndict2
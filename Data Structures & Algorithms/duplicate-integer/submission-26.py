class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nDict = {}

        for indice, numero in enumerate(nums):
            if numero in nDict:
                nDict[numero] += 1
                if nDict[numero] == 2:
                    return True
            else:
                nDict[numero] = 1
        return False
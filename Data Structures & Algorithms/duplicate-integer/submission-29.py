class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = {}
        for n in nums :
            if n in vistos:
                vistos[n]+= 1
                return True
            else:
                vistos[n] = 1
        return False
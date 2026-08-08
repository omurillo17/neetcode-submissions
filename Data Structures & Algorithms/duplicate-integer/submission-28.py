class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = []

        for i in nums:
            if i in vistos:
                return True
            else:
                vistos.append(i)
        
        return False
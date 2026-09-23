class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()

        for i in nums:
            if i in vistos:
                return True
            else:
                vistos.add(i)
        return False
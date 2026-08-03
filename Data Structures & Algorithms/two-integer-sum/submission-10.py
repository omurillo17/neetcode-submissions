class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for i, v in enumerate(nums):
            n = target - v
            if n in vistos:
                return [vistos[n], i]
            vistos[v] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}

        for i, n in enumerate(nums):
            dig = target - n
            if dig in vistos:
                return [vistos[dig], i] 
            
            vistos[n] = i
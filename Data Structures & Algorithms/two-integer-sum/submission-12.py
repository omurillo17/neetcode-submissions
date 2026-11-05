class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in vistos:
                return [vistos[diff], i]
            vistos[nums[i]] = i
        return []               

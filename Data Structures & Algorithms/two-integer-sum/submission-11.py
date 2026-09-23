class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}

        for i in range(len(nums)):
            diferencia = target - nums[i] 
            if diferencia in vistos:
                return [vistos[diferencia], i]
            
            vistos[nums[i]] = i
        return []
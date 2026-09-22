class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            izq = i + 1
            der = len(nums) - 1
            while izq < der:
                tresSum = a + nums[izq] + nums[der]
                if tresSum > 0:
                    der -= 1
                elif tresSum < 0:
                    izq += 1
                else:
                    r.append([a,nums[izq], nums[der]])
                    izq += 1
                    while nums[izq] == nums[izq - 1] and izq < der:
                        izq += 1
        return r
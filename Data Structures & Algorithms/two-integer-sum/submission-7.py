class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diccionario = {}
        for i, n in enumerate(nums):
            resp = target - n
            if resp in diccionario:
                return [diccionario[resp], i]
            diccionario[n] = i
        return 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lista = [1] * n
        prefijo = 1
        for i in range(n):
                lista[i] = prefijo
                prefijo *= nums[i]
                
        sufijo = 1
        for i in range(n - 1, -1, -1):
                lista[i] *= sufijo
                sufijo *= nums[i]
        return lista
            

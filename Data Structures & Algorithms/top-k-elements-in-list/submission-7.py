class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vistos = {}
        res = []
        
        for num in nums:
            if num in vistos:
                vistos[num] += 1
            else:
                vistos[num] = 1
        
        for i in range(k):
            nmax = 0
            nganador = 0

            for llave, valor in vistos.items():
                if valor > nmax:
                    nganador = llave
                    nmax = valor

            res.append(nganador)
            vistos[nganador] = 0
        return res

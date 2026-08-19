class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vistos = {}
        r = []

        for n in nums:
            if n in vistos:
                vistos[n] += 1
            else:
                vistos[n] = 1
        
        for i in range(k):
            nmax = 0
            nganador = 0

            for indice, valor in vistos.items():
                if valor > nmax:
                    nganador = indice
                    nmax = valor

            r.append(nganador)
            vistos[nganador] = 0

        return r
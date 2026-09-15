class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        conteo = {}
        frequencia = [[] for i in range(len(nums) + 1)]

        for n in nums:
            conteo[n] = 1 + conteo.get(n, 0)

        for n, c in conteo.items():
            frequencia[c].append(n)

        res = []

        for i in range(len(frequencia) - 1, 0, -1):
            for n in frequencia[i]:
                res.append(n)
                if len(res) == k:
                    return res

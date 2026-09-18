class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vistos = set(nums)
        masLargo = 0
        for n in nums:
            if (n - 1) not in vistos:
                largo = 0
                while (n + largo) in vistos:
                    largo += 1
                masLargo = max(largo, masLargo)
        return masLargo 
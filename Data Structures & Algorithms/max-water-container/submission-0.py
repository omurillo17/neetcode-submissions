class Solution:
    def maxArea(self, heights: List[int]) -> int:
        izq = 0
        der = len(heights) - 1
        r = 0

        while izq < der:
            area = (der - izq) * min(heights[izq], heights[der])
            r = max(r, area)
            if heights[izq] < heights[der]:
                izq += 1
            else:
                der -= 1
        return r

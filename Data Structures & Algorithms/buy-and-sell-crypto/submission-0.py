class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_max = 0
        p_min = prices[0]
        

        for i in prices:
            if i < p_min:
                p_min = i

            if (i - p_min) > p_max:
                p_max = i - p_min
        return p_max
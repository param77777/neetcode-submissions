class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        res = 0

        while r < len(prices):
            summ = 0
            if prices[l] < prices[r]:
                summ = prices[r] - prices[l]
                res = max(res, summ)
            else:
                l = r
            r += 1
        return res

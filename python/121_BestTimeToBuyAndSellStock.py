class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0;
        buy_point = 0;
        for i, v in enumerate(prices):
            if v<prices[buy_point]:
                buy_point = i
            max_profit = max(v - prices[buy_point], max_profit)
        return max_profit
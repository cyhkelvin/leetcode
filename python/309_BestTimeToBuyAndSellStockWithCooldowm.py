class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = [-prices[0]]
        sell = [0]
        for i in range(1,len(prices)):
            sell.append(max(buy[i-1]+prices[i], sell[i-1]))
            if i>1:
                buy.append(max(buy[i-1], sell[i-2]-prices[i]))
            else:
                buy.append(max(buy[i-1], -prices[i]))
        
        return sell[-1]
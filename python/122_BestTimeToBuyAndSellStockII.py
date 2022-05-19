class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_point, sell_point, sell_profit = 0, 0, 0
        
        for i, v in enumerate(prices):
            if v < max(prices[buy_point], prices[sell_point]):
                if sell_point > buy_point:
                    sell_profit += prices[sell_point] - prices[buy_point]
                buy_point = i
                sell_point = i
            if v > prices[sell_point]:
                sell_point = i
        if sell_point > buy_point:
            sell_profit += prices[sell_point] - prices[buy_point]
        return sell_profit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_point, sell_point, sell_profit = [0], [0], 0
        
        for i, v in enumerate(prices):
            #print('b',buy_point,[prices[i] for i in buy_point])
            #print('s',sell_point,[prices[i] for i in sell_point])
            #print(sell_profit)
            if v < max(prices[buy_point[-1]], prices[sell_point[-1]]):
                if sell_point[-1] > buy_point[-1]:
                    sell_profit += prices[sell_point[-1]] - prices[buy_point[-1]]
                    buy_point.append(i)
                    sell_point.append(i)
                else:
                    buy_point[-1] = i
                    sell_point[-1] = i
            if v > prices[sell_point[-1]]:
                sell_point[-1] = i
        if sell_point[-1] > buy_point[-1]:
            sell_profit += prices[sell_point[-1]] - prices[buy_point[-1]]
        return sell_profit
'''
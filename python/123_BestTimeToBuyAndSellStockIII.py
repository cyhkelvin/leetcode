class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pitch_point = [0]
        
        for i, v in enumerate(prices):
            if v < prices[pitch_point[-1]]:
                if len(pitch_point)%2 == 0:
                    pitch_point.append(i)
                else:
                    pitch_point[-1] = i
            if v > prices[pitch_point[-1]]:
                if len(pitch_point)%2 == 0:
                    pitch_point[-1] = i
                else:
                    pitch_point.append(i)
        
        def OneTradeMaxProfit(pitch_price: List[int]) -> int:
            if len(pitch_price) == 0:
                return 0
            elif len(pitch_price) == 2:
                return pitch_price[1] - pitch_price[0]
            else:
                buyP, maxP = pitch_price[0],0
                for i,v in enumerate(pitch_price):
                    if v < buyP:
                        buyP = v
                    maxP = max(maxP, v-buyP)
                return maxP
        
        if len(pitch_point)%2 == 1:
            del pitch_point[-1]
        pitch_price = [prices[i] for i in pitch_point]
        
        if len(pitch_price) < 3:
            return OneTradeMaxProfit(pitch_price)
        else:
            profit = [OneTradeMaxProfit(pitch_price[:i*2])+OneTradeMaxProfit(pitch_price[i*2:]) for i in range(1,int(len(pitch_price)/2))]
            return max(profit)
        

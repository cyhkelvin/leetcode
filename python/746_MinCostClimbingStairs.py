class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ways = [0, cost[0]]
        for i in range(1,len(cost)):
            ways.append(min(ways[-1], ways[-2])+cost[i])
        return min(ways[-2],ways[-1])
'''
      a, b = cost[0], cost[1]
      for i in range(2, len(cost)):
        temp = min(a, b) + cost[i]
        a = b
        b = temp
      return min(a, b)
'''
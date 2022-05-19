

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        price = [[0]*(n+1) for i in range(n+1)]
        return self.cost(price, 1, n)
    
    def cost(self, dp, l, r):
        if l >= r:
            return 0
        if dp[l][r]:
            return dp[l][r]
        dp[l][r] = min(i + max(self.cost(dp, l, i-1), self.cost(dp, i+1, r)) for i in range(l,r+1))
        return dp[l][r]
        
  '''
n = 20
dp = [[0] * (n + 1) for _ in range(n + 1)]
for l in range(n - 1, 0, -1):
	for r in range(l + 1, n + 1):
		dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))

print(dp[1][n])
'''
import math
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        # 3 <= A.length <= 50
        # 1 <= A[i] <= 100
        dp = [[0]*len(A) for i in range(len(A))]
        # dp = [[0]*len(A)]*len(A) will be wrong!!!
        for n in range(2,len(A)):
            for i in range(len(A)-n):
                minValue = math.inf
                for k in range(i+1,i+n):
                    minValue = min(minValue, (dp[i][k] + dp[k][i+n] + A[i]*A[k]*A[i+n]))
                if not minValue == math.inf:
                    dp[i][i+n] = minValue
        return dp[0][len(A)-1]
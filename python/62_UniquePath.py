class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==1 or j==1:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[-1][-1]

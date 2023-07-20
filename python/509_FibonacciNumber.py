class Solution:
    def fib(self, n: int) -> int:
        # sol1:
        # a = [0]*(n+1)
        # for i in range(1, n+1):
        #     if i == 1:
        #         a[1] = 1
        #     else:
        #         a[i] = a[i-1]+a[i-2]
        # print(a)
        # return a[-1]

        # sol2:
        # a=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        # return a[n]

        # sol3:
        if n < 2:
            return n
        dp = [0, 0, 1]
        for i in range(2, n + 1):
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[0] + dp[1]
        return dp[2]

        # sol4: recursive (pass)
        
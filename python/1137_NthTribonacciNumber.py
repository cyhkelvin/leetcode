class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1, 2]
        if n<=3:
            return t[n]
        for n in range(3, n):
            t[0:3] = t[1:4]
            t[3] = sum(t[:3])
        return t[3]

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        n = int(n/2)
        v = int(n/2)
        while guess(n):
            n = n + v * guess(n)
            v = max(1,int(v/2))
                
        return n
            
        
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>0 else -1
        x *= sign
        res = 0
        while(x>0):
            #print(res,x)
            res += x%10
            res *= 10
            x = int(x/10)
        res = int(res/10)
        if res > pow(2,31)-1:
            return 0
        else:
            return res*sign
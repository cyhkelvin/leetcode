class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        index = 0
        while(index<len(s)):
            r = min(index+k,len(s))
            if int(index/k)%2==0:
                for i in range(r,index,-1):
                    res = res + s[i-1]
            else:
                res+=s[index:r]
            index += k
        return res
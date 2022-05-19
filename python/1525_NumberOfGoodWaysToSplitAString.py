class Solution:
    def numSplits(self, s: str) -> int:
        # my method~
        setChar = set()
        numL = [0]*len(s)
        res = 0
        for i in range(len(s)):
            setChar.add(s[i])
            numL[i] = len(setChar)
        # loop for right tail elements
        setChar = set()
        for i in range(len(s)-1,0,-1):
            setChar.add(s[i])
            if numL[i-1] == len(setChar):
                res += 1
            elif len(setChar) > numL[i-1]:
                break

        return res        
        
        
        
        '''
        #TLE
        atLast, num, res = len(set(s))//2, len(s), 0
        for i in range(atLast, len(s)):
            l = len(set(s[:i]))
            r = len(set(s[i:]))
            if l < atLast:
                continue
            if r < atLast or r > num or l > num:
                break
            if l == r:
                num = l
                res += 1
        return res
        '''
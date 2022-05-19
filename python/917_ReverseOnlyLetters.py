class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        
        def isLetter(c: str) -> bool:
            o = ord(c)
            return 65 <= o <= 90 or 97 <= o <= 122
                
        l,r = 0, len(S)-1
        res = ''
        while(r>l):
            #if not S[l].isalpha(): #slower
            if not isLetter(S[l]): #faster
                res = res[:l] + S[l] + res[l:]
                l += 1
                continue
            #if not S[r].isalpha():
            if not isLetter(S[r]):
                res = res[:l] + S[r] + res[l:]
                r -= 1
                continue
            res = res[:l] + S[r] + S[l] + res[l:]
            l += 1
            r -= 1
        if r == l:
            res = res[:l] + S[r] + res[l:]
            
        return res
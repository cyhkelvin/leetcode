class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        l,r = 0, len(s)-1
        res = ''
        while(r>l):
            if not s[l] in vowels:
                res = res[:l] + s[l] + res[l:]
                l += 1
                continue
            if not s[r] in vowels:
                res = res[:l] + s[r] + res[l:]
                r -= 1
                continue
            res = res[:l] + s[r] + s[l] + res[l:]
            l += 1
            r -= 1
        if r == l:
            res = res[:l] + s[r] + res[l:]
            
        return res
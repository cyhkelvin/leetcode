class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) <= 1:
            return ""
        
        res = ""
        for i in range(len(s)-1):
            if s[i] == s[-1] and s[0] == s[-i-1]:
                if s[:i+1] == s[-i-1:]:
                    res = s[:i+1]
        return res

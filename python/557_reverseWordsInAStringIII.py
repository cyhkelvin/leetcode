class Solution:
    def reverseWords(self, s: str) -> str:
        tmp, res = '', ''
        for i in s:
            if i == ' ':
                res = res + tmp + i
                tmp = ''
            else:
                tmp = i + tmp
        return res + tmp
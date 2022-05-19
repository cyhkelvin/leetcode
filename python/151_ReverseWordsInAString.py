class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        res = ''
        for i in range(len(str_list)):
            #print(str_list[i]+str(i)+str(len(str_list[i])),end=' ')
            if str_list[i]=='':
                continue
            else:
                res = str_list[i] + ' ' + res
                
        return res[:-1]
class Solution:
    def sortString(self, s: str) -> str:
        s_sort = list(set(s))
        s_sort.sort(key = lambda c:ord(c))
        s_dict = {i:0 for i in s_sort}
        res = ""
        for i in s:
            s_dict[i] += 1
        for i in range(len(s)):
            for i in s_sort[::1]:
                res += i
                s_dict[i] -= 1
                if s_dict[i] == 0:
                    s_sort.remove(i)
            for i in s_sort[::-1]:
                res += i
                s_dict[i] -= 1
                if s_dict[i] == 0:
                    s_sort.remove(i)
                
        return res
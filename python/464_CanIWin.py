# dynamic programing, MiniMaxTree
#https://www.cnblogs.com/grandyang/p/6103525.html
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        #maxChoosableInteger <= 20; desiredTotal <= 300
        if maxChoosableInteger >= desiredTotal:
            return True
        elif (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        else:
            self.win_map = {}
            used = '0'*maxChoosableInteger
            return self.Win(maxChoosableInteger, desiredTotal, used)
            
    def Win(self, length: int, total: int, used: str) -> bool:
        if used in self.win_map.keys():
            return self.win_map[used]
        
        else:
            for i in range(length):
                if used[i] == '0':
                    used_cur = used[:i]+'1'+used[i+1:]
                    if (total <= i+1) or (not self.Win(length, total-i-1, used_cur)):
                        self.win_map[used] = True
                        return True
            self.win_map[used] = False
            return False
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{:032b}'.format(n)[::-1],2)
    
        '''
        s = bin(n).replace("0b", "")
        l = len(s)
        s = '0'*(32-l) + s
        s = list(s)
        s.reverse()
        num = int(''.join(s),2)
        return num
        '''
        
        '''
        res = ""
        
        for i in range(32):
            res += str(n%2)
            n = int(n/2)
        res_int = 0
        for i in res:
            res_int += int(i)
            res_int*=2
        
        return int(res_int/2)
        '''
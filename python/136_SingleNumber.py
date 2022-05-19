class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # use property of xor, any number xor with 0 is still itself
        # every number xor with itself will be 0
        # eg: 0 ^ 3 ^ 4 ^ 3 = 4
        xor = 0;
        for i in nums:
            xor ^= i
        return xor
    '''    
        a = {}
        for i in nums:
            try:
                a[i] += 1
            except:
                a[i] = 1
        for i in a.keys():
            if a[i] == 1:
                return i
    '''
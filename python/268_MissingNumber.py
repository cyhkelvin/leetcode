class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumv = len(nums)*(len(nums)+1)*0.5
        return int(sumv-sum(nums))
    '''    
        bstr = '0'*(len(nums)+1)
        for i in nums:
            bstr = bstr[:i]+'1'+bstr[i+1:]
        return bstr.index('0')
    '''
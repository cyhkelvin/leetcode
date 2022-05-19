class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        #return X1/(X2/X3/.../Xn) which means X1/X2*X3*...*Xn will get the maximum.
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return '/'.join([str(i) for i in nums])
        res = str(nums[0])
        res += "/("
        for i in range(1,len(nums)):
            res += str(nums[i])+"/"
        return res[:-1]+")"
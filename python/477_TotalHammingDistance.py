class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # sum up (number of 1s)*(number of 0s) on the position of each digit
        res = 0
        ones, zeros = [0]*32, [0]*32
        for i in range(len(nums)):
            bin_str = '{:032b}'.format(nums[i])
            for i in range(len(bin_str)):
                if bin_str[i] == '0':
                    zeros[i] += 1
                else:
                    ones[i] += 1
        res = sum([ones[i]*zeros[i] for i in range(32)])
        return res
        
        '''
        #Time Limit Exceeded
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                res += bin(nums[i]^nums[j])[2:].count('1')
        return res
        '''
        
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return(nums[int(len(nums)/2)])
    '''    
        times = {}
        if len(set(nums)) == 1:
            return nums[0]
        for i in nums:
            try:
                times[i] += 1
                if times[i] > math.floor(len(nums)/2):
                    return i
            except:
                times[i] = 1
    '''    
    '''  
        times = {i:0 for i in set(nums)}
        for i in nums:
            times[i] += 1
        for i in times.keys():
            if times[i] > math.floor(len(nums)/2):
                return i
    '''
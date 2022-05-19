class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return nums[0]
        profit = [nums[0], max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            profit.append(max(profit[i-2]+nums[i], profit[i-1]))
        return profit[-1]
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = int(len(nums)/2)

        if nums[index] == target:
            return index
        elif nums[index] > target:
            if index == 0:
                return index
            else:
                return Solution().searchInsert(nums[:index], target)
        elif nums[index] < target:
            if index == 0:
                return index + 1
            else:
                return index + Solution().searchInsert(nums[index:], target)
            
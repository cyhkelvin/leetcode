#dp, minimax

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 1 <= length of array <= 20
        # 0 <= number <= 10000000
        # player 1 win if even score
        if len(nums) <= 2:
            return True
        else:
            return self.Win(nums, 0, 0, 1)
        
    def Win(self, nums, sum1, sum2, player):
        if len(nums) == 1:
            if player == 1:
                return sum1+nums[0] >= sum2
            else:
                return sum1 >= sum2+nums[0]
        else:
            if player == 1:
                return self.Win(nums[:-1], sum1+nums[-1], sum2, 2) or self.Win(nums[1:], sum1+nums[0], sum2, 2)
            else:
                return self.Win(nums[:-1], sum1, sum2+nums[-1], 1) and self.Win(nums[1:], sum1, sum2+nums[0], 1)
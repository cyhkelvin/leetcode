from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # num_sort_list = list(set(nums))
        nums = Counter(nums)
        sorted_nums = sorted(nums)
        scores = [0]*len(sorted_nums)
        scores[0] = nums[sorted_nums[0]]*sorted_nums[0]
        ind=1
        for num in sorted_nums[1:]:
            score = nums[num]*num
            if ind == 1:
                if num-sorted_nums[0] == 1:
                    scores[1] = max(scores[0], score)
                else:
                    scores[1] = score + scores[0]
            else:
                if sorted_nums[ind-1] == num-1:
                    # if scores[ind-1] == scores[ind-2]:
                    #     scores[ind] = scores[ind-1] + score
                    # else:
                    #     scores[ind] = max(scores[ind-1], scores[ind-2]+score)
                    scores[ind] = max(scores[ind-1], scores[ind-2]+score)
                else:
                    scores[ind] = scores[ind-1] + score
            ind += 1

        return scores[-1]
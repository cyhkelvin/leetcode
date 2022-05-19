class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = {}
        for i in nums:
            try:
                degree[i] += 1
            except:
                degree[i] = 1
        
        maxV = max(degree.values())
        maxN = []
        for i in degree.keys():
            if degree[i] == maxV:
                maxN.append(i)
        #print(maxN)
        if maxV == 1:
            return 1
        else:
            minL = len(nums)
            L = len(nums)
            for n in maxN:
                for i in range(len(nums)):
                    if nums[i]==n:
                        for j in range(1,len(nums)+1):
                            if nums[-j]==n:
                                minL = min(len(nums[i:L-j+1]), minL)
                                break
                        break
            return minL
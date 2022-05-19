import sys

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [0]
        for i in range(1,len(books)+1):
            width, height = 0, 0
            dp.append(sys.maxsize)
            for j in range(i-1, -1, -1):
                width += books[j][0]
                if width > shelf_width:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j]+height)
        
        return dp[len(books)]
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r, l= n, 1
        while r>l:
            m = int((r+l)/2)
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return r
    
   
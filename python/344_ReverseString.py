class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            tmp = s[i]
            s[i] = s[-1-i]
            s[-1-i] = tmp
            
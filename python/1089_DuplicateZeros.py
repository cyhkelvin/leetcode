class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        tmp = []
        for i in range(len(arr)):
            if arr[i] == 0:
                tmp.append(0)
                tmp.append(0)
            else:
                tmp.append(arr[i])
            arr[i] = tmp[0]
            del tmp[0]
                
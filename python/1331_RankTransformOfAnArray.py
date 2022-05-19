class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_rank = {}
        arr_sort = list(set(arr))
        arr_sort.sort()
        for i in range(len(arr_sort)):
            arr_rank[arr_sort[i]] = i+1
        return [arr_rank[i] for i in arr]
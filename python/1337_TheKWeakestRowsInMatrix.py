class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_weak = []
        for i in range(len(mat)):
            mat_weak.append([i,sum(mat[i])])
        
        bubble_len = len(mat)
        while bubble_len > 1:
            for i in range(bubble_len-1):
                if mat_weak[i+1][1] < mat_weak[i][1]:
                    tmp = mat_weak[i+1]
                    mat_weak[i+1] = mat_weak[i]
                    mat_weak[i] = tmp
            bubble_len -= 1
        
        kWeakestRow = []
        for i in range(k):
            kWeakestRow.append(mat_weak[i][0])
        return kWeakestRow
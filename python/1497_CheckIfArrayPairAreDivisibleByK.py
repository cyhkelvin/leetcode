#rewrite if have time

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr_k = [0]*k
        for i in arr:
            arr_k[i%k]+=1
        for i in range(1,k):
            if arr_k[i] != arr_k[k-i]:
                return False
            if k%2 == 0:
                if not (arr_k[int(k/2)]%2 == 0):
                    return False
        return True
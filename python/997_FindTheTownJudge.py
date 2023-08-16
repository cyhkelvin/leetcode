class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        vote = dict()
        for i in range(n):
            vote[i+1] = 0

        for rel in trust:
            if rel[0] in vote.keys():
                del vote[rel[0]]
            if rel[1] in vote.keys():
                vote[rel[1]] += 1

        candidate = -1
        for k, v in vote.items():
            if v == n-1:
                if candidate != -1:
                    return -1
                else:
                    candidate = k
        return candidate


## cool method
    # def findJudge(self, n: int, trust: List[List[int]]) -> int:
    #     Trusted = [0] * (n+1)
    #     for (a, b) in trust:
    #         Trusted[a] -= 1
    #         Trusted[b] += 1
            
    #     for i in range(1, len(Trusted)):
    #         if Trusted[i] == n-1:
    #             return i
    #     return -1
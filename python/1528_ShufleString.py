class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_dict = {indices[i]:i for i in range(len(indices))}
        return ''.join([s[s_dict[i]] for i in range(len(indices))])
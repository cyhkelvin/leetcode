class Solution:

    # sol0: Time Limit Exceed
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     if s in wordDict:
    #         return True
    #     # "aaaaaaaaaaaaaaa...aaaaaab"
    #     # ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    #     lenList = [len(x) for x in wordDict]
    #     minLen = min(lenList)
    #     if len(s) <= minLen:
    #         return False
    #     maxLen = max(lenList)
    #     for subWordLen in range(maxLen, minLen-1, -1):
    #         if s[:subWordLen] in wordDict:
    #             if self.wordBreak(s[subWordLen:], wordDict):
    #                 return True
    #     return False

    # sol1: pass (record false words)
    # runtime: 96.61%(43ms) memory: 60.8%(16.4mb)
    def __init__(self):
        super().__init__()
        self.falseWord = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        if s in self.falseWord:
            return False
        subWord = [word for word in wordDict]
        if len(subWord) == 0:
            self.falseWord.add(s)
            return False
       
        lenList = [len(x) for x in subWord]
        minLen = min(lenList)
        if len(s) <= minLen:
            self.falseWord.add(s)
            return False
        maxLen = max(lenList)
        for subWordLen in range(maxLen, minLen-1, -1):
            if s[0-subWordLen:] in subWord:
                if self.wordBreak(s[:len(s)-subWordLen], subWord):
                    return True
        self.falseWord.add(s)
        return False

    # sol2: dynamic programming
    # runtime 16.67%(64ms) memory:84.8%(16.31mb)
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     dp = [False] * (len(s)+1)
    #     dp[0] = True
    #     wordDict = set(wordDict)

    #     for i in range(len(s)+1):
    #         for j in range(i):
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break

    #     return dp[-1]
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxSen= 0
        for i in sentences:
            maxSen=max(maxSen, i.count(" ")+1)
        return maxSen
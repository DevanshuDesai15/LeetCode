class Solution:
    def numJewelsInStones(self, j: str, S: str) -> int:
        setJ = set(j)
        return sum(s in setJ for s in S)
    
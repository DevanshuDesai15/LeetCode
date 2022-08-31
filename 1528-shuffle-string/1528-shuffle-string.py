class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s) # A list is used here to store character
        for i,c in enumerate(s):
            result[indices[i]] = c
        return "".join(result) # joined to get the result
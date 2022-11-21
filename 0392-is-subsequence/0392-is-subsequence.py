class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initialise two pointer
        i,j = 0,0
        
        # run the loop untill i,j are less then len of both strings
        while i < len(s) and j < len(t):
            # comparing the strings
            if s[i] == t[j]:
                i+=1
            j+=1
                
        return True if i == len(s) else False
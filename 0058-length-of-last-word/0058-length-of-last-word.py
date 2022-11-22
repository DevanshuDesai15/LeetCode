class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # initialise pointer 
        i, length = len(s) - 1, 0
        
        # start loop from back to the first space
        while s[i] == " ":
            i -= 1
        # counting the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
        
        # here split can be used but it becomes a bit of a cheating!!!
        # t = s.split()
        # return len(t[-1])
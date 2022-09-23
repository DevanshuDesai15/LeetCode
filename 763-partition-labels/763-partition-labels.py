class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex ={} # creating hash map
        
        for i, c in enumerate(s): # will check both index and character at the same time
            lastIndex[c]=i # last index of this character
        
        res=[] # to store output
        size, end = 0, 0
        for i,c in enumerate(s):
            size += 1 # increment size after checking of every character
            end = max(end, lastIndex[c]) # if lastIndex is > then end then update end to be max of itself
            
            if i == end:    # index and end becomes same add size to result
                res.append(size)
                size = 0
        return res
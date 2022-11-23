class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # make an empty string
        res = ""
        
        # iterate through the 1st string in array
        for i in range(len(strs[0])):
            for s in strs: # now checking the strings
                if i == len(s) or s[i] != strs[0][i]: # if out of bound or first letter dosent match
                                                        # return empty result
                    return res
            res += strs[0][i] # add first letter in the result if same
        return res 
        
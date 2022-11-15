class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # using hash Map
        
        # first check the length of both the strings
        if len(s) != len(t):
            return False
        
        # HashMaps
        countS, countT = {}, {}
        
        # creting the hashMap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # get is used because if no same keyValue pair
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # now checking both the maps
        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count ={}
        res, maxCount = 0, 0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0) # increment count by 1
            res = n if count[n] > maxCount else res
            # if count is > then maxCount then update the result to n or if the maxCOunt is equal then we can keep the result 
            maxCount = max(count[n], maxCount) # count of maxCount 
        return res
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # log(n)
        l,r = 0, len(nums) -1 # left and right pointer
        
        while l<=r:
            mid = (l+r) //2
            
            if target == nums[mid]: # check first
                return mid
            
            if target > nums[mid]: # if target is big then middle 
                l = mid +1 # start search to right
            else: # target is less then middle
                r = mid -1 # start search left
             
        return l # never found a target 
    # Why left?? not right
    # if left crosses right then assign left index
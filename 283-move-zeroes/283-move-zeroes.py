class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left =0
        for right in range(len(nums)): #4 right will increment with for loop
            if nums[right]: #1 if right num is non-zero
                nums[left], nums[right] = nums[right], nums[left]
                #2 above swaping the left index with right index
                left += 1 #3 incrementing the left pointer
        return nums
     
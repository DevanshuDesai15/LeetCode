class Solution:
    def pivotIndex(self, nums):
        sumL = 0
        sumR = sum(nums)
        for i in range (len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1
        
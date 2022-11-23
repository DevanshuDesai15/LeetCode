class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Here the time complexity is O(n)
        
        # make a hashMap
        hashMap={} # value : index
        
        # take the diff of target and n 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return
    
        
        # Complexity is O(n2) 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for n in nums:
            res = n ^ res # doing an XOR operation as 1 ^ 1 = 0 and we can simplify it by 
                          # n ^ 1/0 = n
        return res
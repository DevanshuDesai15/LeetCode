class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = 0,0
        
        for n in nums:
            # if the count sets to 0 then res is n
            if cnt == 0:
                res = n
            
            #if number is same as res then count +1 and not count-1
            if n == res:
                cnt+=1
            else:
                cnt-= 1
        
        return res
            
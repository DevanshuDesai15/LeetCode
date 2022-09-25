class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 # left=buying right=selling
        maxP=0 # max Profit
        
        while r < len(prices): # itterate till right pointer not passed end of prices
            # profitable ???
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] # calculate profit
                maxP = max(maxP, profit) # find max between current max and new profit
            else: # not profitable
                l = r  # update left pointer to the right
            r +=1
        return maxP
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth=0
        for i in range (len(accounts)):
            totWealth = sum(accounts[i])
            maxWealth = max(maxWealth, totWealth)
        return maxWealth
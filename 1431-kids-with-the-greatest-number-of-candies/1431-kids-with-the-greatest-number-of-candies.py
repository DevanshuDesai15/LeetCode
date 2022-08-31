class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        outcome = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                outcome.append(True)
            else:
                outcome.append(False)
        return outcome
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minb=prices[0]
        for sell in prices[1:]:
            maxp=max(maxp,sell-minb)
            minb=min(minb,sell)
        return maxp
            
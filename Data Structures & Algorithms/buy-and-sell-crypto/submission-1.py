class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        maxp = 0
        for curr_price in prices[1:]:
            if curr_price<min_price:
                min_price=curr_price
            else:
                curr_profit = curr_price - min_price
                if curr_profit>maxp:
                    maxp=curr_profit
        return maxp




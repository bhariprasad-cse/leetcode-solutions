class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        pro = 0
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            pro = prices[i]-buy
            ans = max(ans, pro)
        return ans
        
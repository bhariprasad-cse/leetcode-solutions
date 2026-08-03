# LeetCode 121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        min_price = min(prices)
        dic = []
        for i in range(prices[min_price], len(prices)):
            profit = prices[i] - min_price
            dic.append(profit)
        print(max(dic))
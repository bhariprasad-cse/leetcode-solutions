# LeetCode 643 - Maximum Average Subarray I
# Difficulty: Easy
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum = 0
        for i in range(len(nums)):
            if i < k:
                cur_sum += nums[i]
                ans = cur_sum
            else:
                cur_sum -= nums[i-k]
                cur_sum += nums[i]
            ans = max(ans, cur_sum)
        return ans/k
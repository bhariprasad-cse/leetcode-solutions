# LeetCode 53 - Maximum Subarray
# Difficulty: Medium
# Topic: Dynamic Programming
# Time Complexity: O(n²) (Current Solution)
# Space Complexity: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        ans = 0
        cur_sum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
            cur_sum = 0
        print(ans)
# LeetCode 3 - Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            last_seen[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans
# LeetCode 169 - Majority Element
# Difficulty: Easy
# Topic: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        if max(freq.values()) > len(nums)/2:
            return [key for key, value in freq.items() if value == max(freq.values())]
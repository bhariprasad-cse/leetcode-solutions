# LeetCode 283 - Move Zeroes
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        return nums
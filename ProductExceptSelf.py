# LeetCode 238 - Product of Array Except Self
# Difficulty: Medium
# Topic: Prefix & Suffix
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)

class Solution(object):
    def productExceptSelf(self, nums):
        prefix = 1
        suffix = 1
        nums1 = []
        for i in range(0, len(nums)):
            x = nums[i]
            nums1.append(prefix)
            prefix *= x
        for j in range(len(nums)-1, -1, -1):
            nums1[j] *= suffix
            suffix *= nums[j]
        return nums1
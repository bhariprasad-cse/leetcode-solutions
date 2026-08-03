# LeetCode 349 - Intersection of Two Arrays
# Difficulty: Easy
# Topic: Hash Set
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

class Solution(object):
    def intersection(self, nums1, nums2):
        nums3 = set(nums1)
        nums4 = set(nums2)
        return nums3.intersection(nums4)
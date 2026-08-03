# LeetCode 1 - Two Sum
# Difficulty: Easy
# Topic: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        map={}
        for index, value in enumerate(nums):
            x = target - value
            if x in map:
                return [index, map[x]]
            map[value] = index
# LeetCode 26 - Remove Duplicates from Sorted Array
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j+=1
        return j+1
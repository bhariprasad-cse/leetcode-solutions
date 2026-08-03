# LeetCode 35 - Search Insert Position
# Difficulty: Easy
# Topic: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        upper = len(nums)-1
        lower = 0
        while lower<=upper:
            mid = (lower+upper)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lower = mid+1
            else:
                upper = mid-1
        return lower
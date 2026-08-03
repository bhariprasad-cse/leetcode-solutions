# LeetCode 704 - Binary Search
# Difficulty: Easy
# Topic: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        upper = len(nums)-1
        lower = 0
        while target >= nums[lower] and target <= nums[upper]:
            mid = (upper+lower)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                lower = mid+1
            else:
                upper = mid-1
        return -1
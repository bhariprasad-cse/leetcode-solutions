# LeetCode 69 - Sqrt(x)
# Difficulty: Easy
# Topic: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        upper = x
        lower = 0
        while lower<=upper:
            mid = (upper+lower)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                upper = mid-1
            else:
                lower = mid+1
        return upper
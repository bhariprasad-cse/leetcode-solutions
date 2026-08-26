class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower, upper = 0, len(nums)-1
        while lower<upper:
            mid = (lower+upper)//2
            if nums[lower] <= nums[upper]:
                return nums[lower]
            elif nums[mid] >= nums[lower]:
                lower = mid+1
            else:
                upper = mid
        return nums[lower]
        
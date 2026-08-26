class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)-1
        while lower<=upper:
            mid = (lower+upper)//2
            if nums[mid] == target:
                return mid
            if nums[lower] <= nums[mid]:
                if target < nums[lower] or target > nums[mid]:
                    lower = mid+1
                else:
                    upper = mid-1
            else:
                if target < nums[mid] or target > nums[upper]:
                    upper = mid-1
                else:
                    lower = mid+1
        return -1
# LeetCode 88 - Merge Sorted Array
# Difficulty: Easy
# Topic: Two Pointers
# Time Complexity: O(m+n)
# Space Complexity: O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        for x in range(0, m+n):
            if j >= 0 and nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            elif i >= 0:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        return nums1
sol = Solution()
ans = sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(ans)
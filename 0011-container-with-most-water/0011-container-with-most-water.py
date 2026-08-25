class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0
        while l<r:
            if height[l] <= height[r]:
                curArea = height[l]*(r-l)
                l+=1
            else:
                curArea = height[r]*(r-l)
                r-=1
            res = max(res, curArea)
        return res
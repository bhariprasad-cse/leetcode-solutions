class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        output = []
        #prefix
        for i in range(1,len(nums)+1):
            output.append(pre)
            pre *= nums[i-1]
        #postfix
        pos = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= pos
            pos *= nums[i]
        return output


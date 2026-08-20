class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = {}
        max_value = 0
        for n in nums:
            check[n] = check.get(n, 0)+1
            key = max(check, key=check.get)
        return key
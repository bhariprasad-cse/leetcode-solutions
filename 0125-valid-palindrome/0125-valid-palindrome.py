class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        ls = s.lower()
        for c in ls:
            if (ord('a') <= ord(c) <= ord('z') or (ord('0') <= ord(c) <= ord('9'))):
                stack.append(c)
        reverse_stack = stack[::-1]
        return reverse_stack == stack
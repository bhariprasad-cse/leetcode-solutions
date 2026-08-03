# LeetCode 242 - Valid Anagram
# Difficulty: Easy
# Topic: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
        for j in range(len(t)):
            if t[j] in freq:
                freq[t[j]] = freq.get(t[j])-1
        if all(value == 0 for value in freq.values()):
            return True
        return False
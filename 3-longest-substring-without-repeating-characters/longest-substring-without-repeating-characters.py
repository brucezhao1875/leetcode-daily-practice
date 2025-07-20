class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        result = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in char_index and char_index[c] >= left:
                left = char_index[c] + 1
            char_index[c] = right
            result = max(result,right-left+1)

        return result
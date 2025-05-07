class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        start = 0
        result = []
        while start < n :
            while start<n and s[start] == ' ' : start += 1
            end = start + 1
            while end<n and s[end] != ' ' : end += 1
            if start<end and start < n and s[start] != ' ' : result.append(s[start:end])
            start = end
        result.reverse()
        print(result)
        return ' '.join(result)
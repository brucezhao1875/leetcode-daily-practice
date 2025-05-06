class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        result = 0
        for i in range(n):
            result = max(min(citations[i],n-i),result)
        return result
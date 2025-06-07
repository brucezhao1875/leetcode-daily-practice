class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 : return s
        result = [ '' for _ in range(numRows) ]
        delta = 1
        row = 0
        for c in s:
            result[row] += c
            row += delta
            if row==0 or row==numRows-1 : delta = -delta

        return ''.join(result)
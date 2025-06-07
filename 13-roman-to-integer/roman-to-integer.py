class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }
        result = 0
        n = len(s)
        index = 0
        while index < n :
            if index <= n-2 and s[index:index+2] in hash:
                result += hash.get(s[index:index+2])
                index += 2
            else:
                result += hash.get(s[index:index+1])
                index += 1

        return result
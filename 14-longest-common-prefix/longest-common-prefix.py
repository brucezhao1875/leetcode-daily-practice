class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def maxLen(strs):
            n = len(strs[0])
            for str in strs:
                n = min(n,len(str))
            print("min len,",n)
            for i in range(n):
                c = strs[0][i]
                for str in strs:
                    if str[i] !=  c :
                        return i
            return n
        
        n = maxLen(strs)
        return strs[0][0:n]
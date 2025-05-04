class Solution:
    #
    # 暴力解法：逐个元素比较。复杂度:O(s*t) = O(10^6)，
    # 很有意思，实际上这个递归复杂度不止O(10^6), timeout。为什么会想到这种方法，
    # 这种思路有缺陷：假设s的首字符是a，在t中有多个地方匹配。那么只要将s,t的指针都往前走一步，不需要再关心下一个匹配a的位置了。
    # 按照这个思路，提出双指针。
    #
    def isSubsequence2(self, s: str, t: str) -> bool:
        
        def substr(s,t):
            if len(s) == 0 : return True
            if len(t) == 0 : return False
            result = False
            n = len(t)
            for i in range(n):
                if t[i] == s[0]:
                    result = result or substr(s[1:],t[i+1:])
                    if result is True: break
            return result
        
        return substr(s,t)

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i==len(s)

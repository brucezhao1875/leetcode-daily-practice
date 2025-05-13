class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = []
        for x in s:
            if x.isalnum() :
                s_.append(x.lower())
        n = len(s_)
        for i in range(n//2):
            if s_[i] != s_[n-1-i]:
                return False
        return True


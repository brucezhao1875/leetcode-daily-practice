class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def kmp(s,t):
            pi = [0 for _ in range(len(t))]
            cnt = 0
            for i in range(1,len(t)):
                while cnt > 0 and t[cnt] != t[i]:
                    cnt = pi[cnt-1]
                if t[i] == t[cnt] :
                    cnt += 1
                pi[i] = cnt
            cnt = 0
            for i in range(len(s)):
                while cnt>0 and t[cnt] != s[i]:
                    cnt = pi[cnt-1]
                if s[i] == t[cnt]:
                    cnt += 1
                if cnt == len(t):
                    return i - cnt + 1
            return -1
        
        return kmp(haystack,needle)
        
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        need_features = collections.Counter(t)
        real_features = collections.Counter()
        valid = 0 # 符合条件的字符类计数。当 valid==len(need_features)时，表示当前的窗口符合所需特征
        start,end = 0, max(len(s),len(t)) + 1
        left = 0
        for right in range(len(s)):
            x = s[right]
            if need_features[x] > 0 : 
                real_features[x] += 1
                if real_features[x] == need_features[x] : valid += 1  #突变
            while valid == len(need_features):
                if right-left < end - start : end,start = right,left
                x = s[left]
                left += 1
                if need_features[x] > 0 :
                    if real_features[x] == need_features[x] : valid -= 1  #突变
                    real_features[x] -= 1
        if end == max(len(s),len(t)) + 1 : 
            return ""
        else :
            return s[start:end+1]

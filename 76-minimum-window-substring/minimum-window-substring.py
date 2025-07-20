class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_features = collections.Counter(t)
        window_features = collections.Counter()
        valid = 0
        start,end = 0, max(len(s),len(t)) + 1
        left = 0
        for right in range(len(s)):
            ch = s[right]
            if need_features[ch] : 
                window_features[ch] += 1
                if window_features[ch] == need_features[ch]:
                    valid += 1
            while valid == len(need_features):
                if right-left < end-start:
                    start,end = left,right
                ch = s[left]
                left += 1
                if need_features[ch] > 0:
                    if window_features[ch] == need_features[ch]:
                        valid -= 1
                    window_features[ch] -= 1
        if end == max(len(s),len(t)) + 1 :
            return ""
        else:
            return s[start:end+1]        



    def minWindow2(self, s: str, t: str) -> str:
        need_features = collections.Counter(t)
        window_features = collections.Counter()
        valid = 0 # 多少类字母匹配好了,valid == len(need_features)时，表示完全匹配
        start,end = 0,max(len(s),len(t))+1

        left = 0
        for right in range(len(s)):
            ch = s[right]
            if need_features[ch]:
                window_features[ch] += 1
                if window_features[ch] == need_features[ch]: #在变化的开关瞬间，进行一次valid++的运算
                    valid += 1
            while valid == len(need_features) :
                if right-left< end-start:
                    end,start = right,left
                ch = s[left]
                left += 1
                if need_features[ch] > 0:
                    if window_features[ch] == need_features[ch]:
                        valid -= 1 #在变化的开关瞬间，进行一次valid--的运算
                    window_features[ch] -= 1
        if end == max(len(s) , len(t)) + 1:
            return ""
        else:
            return s[start:end+1]            
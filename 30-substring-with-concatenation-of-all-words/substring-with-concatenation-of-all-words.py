class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l,m,n = len(s),len(words[0]),len(words)
        result = []
        features = Counter()
        for i in range(n):
            features[words[i]] += 1
        for i in range(m):
            tmp_features = Counter()
            match_cnt = 0
            left = i
            right = i
            while right +m <= l:
                x = s[right:right+m]
                right += m
                if x in features:
                    tmp_features[x] += 1
                    match_cnt += 1
                    while tmp_features[x] > features[x]:
                        del_word = s[left:left+m]
                        tmp_features[del_word] -= 1
                        left += m
                        match_cnt -= 1
                else:
                    left = right
                    tmp_features.clear()
                    match_cnt = 0
                if match_cnt == n:
                    result.append(left)
        return result


    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        l,m,n = len(s),len(words[0]),len(words)
        result = []
        global_features = Counter()
        for i in range(n):
            global_features[words[i]] += 1
        
        for i in range(m):
            tmp_features = Counter()
            match_cnt = 0
            left = i
            right = i
            while right + m <= l:
                x = s[right:right+m]
                right += m
                if x in global_features:
                    tmp_features[x] += 1
                    match_cnt += 1
                    while tmp_features[x] > global_features[x]:
                        del_word = s[left:left+m]
                        tmp_features[del_word] -= 1
                        left += m
                        match_cnt -= 1
                else:
                    left = right
                    tmp_features.clear()
                    match_cnt = 0
                if match_cnt == n:
                    result.append(left)
        return result
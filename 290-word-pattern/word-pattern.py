class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        def features(list):
            result = []
            maps = {}
            feature_idx = 0
            for x in list:
                if x not in maps:
                    maps[x] = str(feature_idx)
                    feature_idx += 1
                result.append(maps[x])
            return ''.join(result)                    

        
        return features([x for x in pattern]) == features(s.split())
        
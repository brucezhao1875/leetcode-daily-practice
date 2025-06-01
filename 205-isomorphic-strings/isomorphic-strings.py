class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        map = {}
        for i in range(n):
            key = s[i]
            if key not in map.keys():
                map[key] = t[i]
            else:
                if map[key] != t[i]:
                    return False
        map = {}
        for i in range(n):
            key = t[i]
            if key not in map.keys():
                map[key] = s[i]
            else:
                if map[key] != s[i]:
                    return False

        return True

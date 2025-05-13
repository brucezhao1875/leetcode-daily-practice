class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_stat = {}
        for x in s:
            s_stat[x] = s_stat.get(x) + 1 if x in s_stat else 0
        t_stat = {}
        for x in t:
            t_stat[x] = t_stat.get(x) + 1 if x in t_stat else 0
        for x in s_stat.keys():
            if s_stat.get(x) != t_stat.get(x):
                return False
        for x in t_stat.keys():
            if s_stat.get(x) != t_stat.get(x):
                return False
        return True
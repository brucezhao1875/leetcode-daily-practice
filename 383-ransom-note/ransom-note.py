class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = {}
        for c in ransomNote:
            x[c] = x.get(c) + 1  if c in x else 1
        y = {}
        for c in magazine:
            y[c] = y.get(c) + 1 if c in y else 1
        
        for key in x.keys():
            if not y.get(key) or y.get(key)<x.get(key) : 
                return False
        return True
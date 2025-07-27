class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getKey(str):
            return ''.join(sorted(str))

        hash = {}
        for t in strs:
            key = getKey(t)
            if key not in hash:
                hash[key] = []
            hash[key].append(t)
        
        return list(hash.values())

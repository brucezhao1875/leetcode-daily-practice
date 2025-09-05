class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}

        for num in nums :
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
                
        for key in counter.keys():
            if counter[key] == 1 :
                return key
        
        return -1
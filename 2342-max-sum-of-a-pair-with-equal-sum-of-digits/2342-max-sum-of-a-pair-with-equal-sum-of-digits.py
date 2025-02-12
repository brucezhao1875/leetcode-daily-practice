class Solution:
    '''
    以sum of digits 为key，分为多个queue；挑选len>2的queue，取其最大的[0,1]俩num相加；取max值。
    '''
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(num):
            result = 0
            while num:
                result += num % 10
                num = num // 10
            return result

        nums.sort(reverse=True)

        map = {}
        for i,num in enumerate(nums):
            key = sum_of_digits(num)
            value = map.get(key,[])
            value.append(i)
            map[key] = value
        
        result = -1
        for key in map.keys():
            value = map[key]
            if len(value) <= 1 : continue
            result = max(result,nums[value[0]] + nums[value[1]])
        
        return result
        
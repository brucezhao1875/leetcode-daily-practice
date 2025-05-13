class Solution:
    #这个方法借助了prefix和suffix，看起来轻巧一些。
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]
        prefix = 1
        suffix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        zero_indices = [index for index,num in enumerate(nums) if num==0]
        if len(zero_indices) >= 2 : return result
        elif len(zero_indices) == 1 :
            product = reduce(lambda x,y:x*y , filter(lambda n : n!=0 , nums))
            result[zero_indices[0]] = product
            return result
        else:
            product = reduce(lambda x,y:x*y,nums)
            result = [ product // nums[i] for i in range(n) ]
            return result
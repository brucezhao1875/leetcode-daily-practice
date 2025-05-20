class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        dict_num_pos = {}
        for i,x in enumerate(nums):
            dict_num_pos[x] = i
        sum_of_digits = lambda x:sum(int(digit) for digit in str(x))
        nums.sort(key=lambda x:(sum_of_digits(x),x))
        
        #1. convert nums into array of 0,1,2,...,n-1 , which is not in ascend order
        tmp_nums = [0 for _ in range(n)]
        for i,x in enumerate(nums):
            tmp_nums[dict_num_pos[x]] = i
        nums = tmp_nums
        dict_num_pos = {}
        for i,x in enumerate(nums):
            dict_num_pos[x] = i
        #print(nums,"#",dict_num_pos)
        
        #2. calc the minimum swaps to change the array into ascend order  
        result = 0
        for i in range(n):
            if nums[i] == i : continue
            result += 1
            tmp = nums[i]
            nums[i] = i
            nums[dict_num_pos[i]] = tmp
            
            tmp_pos = dict_num_pos[i]
            dict_num_pos[i] = i
            dict_num_pos[tmp] = tmp_pos
        
        #3.return result
        return result
            
                
        
        
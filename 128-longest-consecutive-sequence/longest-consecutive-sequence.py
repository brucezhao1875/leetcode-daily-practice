class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0
        
        nums.append(inf)  # 在尾巴增加一个元素，这样循环的函数中不用考虑最后一个跳变的逻辑问题
        nums = sorted(set(nums))

        max_length = 1
        current_length = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1 :
                current_length += 1
            else:
                max_length = max(max_length,current_length)
                current_length = 1

        return max_length
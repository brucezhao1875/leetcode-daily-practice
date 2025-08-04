class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # 确保左边包含中位数（奇偶皆可）

        left, right = 0, m  # 在 nums1 中二分
        while left <= right:
            i = (left + right) // 2
            j = total_left - i  # nums2 中的对应分割

            nums1_left_max  = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf')  if i == m else nums1[i]
            nums2_left_max  = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf')  if j == n else nums2[j]

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 分割点正确，计算中位数
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
        return 0            
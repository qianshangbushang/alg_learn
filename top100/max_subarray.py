#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :max_subarray.py
# @Time      :2022/7/9 9:27


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        a, result = 0, -10000
        for x in nums:
            a = a + x
            result = result if result > a else a
            a = a if a > 0 else 0
        return result

    def maxSubArray3(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        a, result = max(0, nums[0]), nums[0]

        for idx in range(1, len(nums)):
            a = a + nums[idx]
            result = max(a, result)
            a = max(a, 0)
        return result

    def maxSubArray2(self, nums: List[int]) -> int:
        """
        输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
        输出：6
        解释：连续子数组 [4,-1,2,1] 的和最大，为 6
        :param nums:
        :return:
        """
        result = nums[0]
        dp = [nums[0]]
        for idx in range(1, len(nums)):
            dp.append(max(dp[idx - 1] + nums[idx], nums[idx]))
            result = max(result, dp[idx])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

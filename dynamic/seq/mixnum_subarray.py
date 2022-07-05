#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :mixnum_subarray.py
# @Time      :2022/7/5 14:42


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i]: 包括下标i在内的之前最长序列和
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        :param nums:
        :return:
        """

        dp = [0 for _ in range(len(nums) + 1)]
        result = nums[0]
        for idx in range(1, len(nums) + 1):
            dp[idx] = max(dp[idx - 1] + nums[idx - 1], nums[idx - 1])
            result = max(dp[idx], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

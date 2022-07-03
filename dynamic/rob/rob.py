#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rob.py
# @Time      :2022/7/3 23:44


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i]: 前i个数组合成的最大数

        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for idx in range(2, len(nums) + 1):
            dp[idx] = max(dp[idx - 2] + nums[idx - 1], dp[idx - 1])

        return dp[len(nums)]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))

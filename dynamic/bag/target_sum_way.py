#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :target_sum_way.py
# @Time      :2022/7/2 19:45


from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        所有数据可以分成两部分，一部分放+， 一部分放-
        left - (sum - left) = target
        left = 1/2(sum + target)

        dp[i]: 容量为i有几种填充方法
        dp[i] += dp[i - x]
        :param nums:
        :param target:
        :return:
        """
        sum_all = sum(nums)
        if sum_all < target or -sum_all > target:
            return 0

        if (sum_all + target) % 2 != 0:
            return 0
        sum_target = (sum_all + target) // 2
        dp = [0] * (sum_target + 1)
        dp[0] = 1

        for x in nums:
            y = sum_target
            while y >= x:
                dp[y] += dp[y - x]
                y -= 1
        return dp[sum_target]


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([100], -200))

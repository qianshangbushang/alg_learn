#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :can_partition.py
# @Time      :2022/7/2 19:17


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        dp[i]  背包大小为i时，最大装入数据

        dp[i] = max(dp[i],  dp[i - nums[j]] + nums[j])

        :param nums:
        :return:
        """

        sum_val = sum(nums)
        if sum_val % 2 != 0:
            return False
        dp = [0] * (sum_val // 2 + 1)
        for x in nums:
            y = sum_val // 2
            while y >= x:
                dp[y] = max(dp[y], dp[y - x] + x)
                y -= 1
        return dp[-1] == sum_val // 2


if __name__ == '__main__':
    s = Solution()

    print(s.canPartition([1, 5, 11, 5]))
    print(s.canPartition([1, 2, 3, 5]))

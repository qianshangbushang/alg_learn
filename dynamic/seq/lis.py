#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lis.py
# @Time      :2022/7/4 16:33


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i]  i之前的最长递增序列长度
        dp[i] = max(dp[j]+ 1)
        :param nums:
        :return:
        """
        dp = [1] * len(nums)
        result = dp[0]
        for idx in range(1, len(nums)):
            for idy in range(0, idx):
                if nums[idy] < nums[idx]:
                    dp[idx] = max(dp[idx], dp[idy] + 1)
                result = max(dp[idx], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([7] * 5))
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))

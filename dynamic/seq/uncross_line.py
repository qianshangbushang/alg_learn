#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :uncross_line.py
# @Time      :2022/7/5 14:36


from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        不连续，利用周边进行传递
        dp[i][j] = dp[i-1][j-1] + 1
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        :param nums1:
        :param nums2:
        :return:
        """

        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxUncrossedLines([1, 4, 2], [1, 2, 4]))

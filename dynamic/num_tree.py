#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :num_tree.py
# @Time      :2022/7/2 10:47


class Solution:
    def numTrees(self, n: int) -> int:
        """
        dp[i]  i个节点的搜索树个数
        :param n:
        :return:
        """

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for idx in range(3, n + 1):
            dp[idx] = sum(dp[idy - 1] * dp[idx - idy] for idy in range(1, idx + 1))

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))

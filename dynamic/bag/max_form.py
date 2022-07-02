#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :max_form.py
# @Time      :2022/7/2 20:26


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        dp[m][n]:  满足条件的最大子集长度
        dp[m][n] = max(dp[m][n], dp[m-x_m][m-x_n] + 1)
        :param strs:
        :param m:
        :param n:
        :return:
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            s_0 = s.count('0')
            s_1 = s.count('1')
            x = m
            while x >= s_0:
                y = n
                while y >= s_1:
                    dp[x][y] = max(dp[x][y], dp[x - s_0][y - s_1] + 1)
                    y -= 1
                x -= 1
            # print(*dp, sep='\n', end='\n\n')
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))

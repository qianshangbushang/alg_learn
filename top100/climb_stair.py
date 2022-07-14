#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :climb_stair.py
# @Time      :2022/7/14 10:55


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2

        for _ in range(3, n + 1):
            b, a = a + b, b

        return b

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))

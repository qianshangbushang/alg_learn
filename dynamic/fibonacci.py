#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fibonacci.py
# @Time      :2022/7/2 8:39


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            # arr.append(arr[i - 1] + arr[i - 2])
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))

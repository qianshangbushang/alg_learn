#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :combination.py
# @Time      :2022/7/7 14:03


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        77. https://leetcode.cn/problems/combinations/

        :param n:
        :param k:
        :return:
        """

        result = []

        def track(path: List[int], start: int, end: int):
            if len(path) == k:
                result.append(path.copy())
                return

            for x in range(start + 1, end + 2 - k + len(path)):
                path.append(x)
                track(path, x, end)
                path.pop()
            return

        track([], 0, n)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))

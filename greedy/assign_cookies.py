#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :assign_cookies.py
# @Time      :2022/7/8 10:43


from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(key=lambda x: x)
        s.sort(key=lambda x: x)

        idx_g, idx_s = 0, 0
        result = 0
        while idx_g < len(g) and idx_s < len(s):
            if g[idx_g] <= s[idx_s]:
                result += 1
                idx_g += 1
            idx_s += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))
    print(s.findContentChildren([1, 2], [1, 2, 3]))

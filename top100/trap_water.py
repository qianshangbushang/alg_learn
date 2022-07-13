#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :trap_water.py
# @Time      :2022/7/13 10:52


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_h = [0] * len(height)
        for idx in range(1, len(height)):
            left_h[idx] = max(left_h[idx - 1], height[idx - 1])
            # left_h.append(max(left_h[idx - 1], height[idx - 1]))

        right_h = [0] * len(height)
        for idx in range(len(height) - 2, -1, -1):
            right_h[idx] = max(right_h[idx + 1], height[idx + 1])
        result = 0
        for idx, he in enumerate(height):
            h = min(left_h[idx], right_h[idx]) - he
            result += max(h, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

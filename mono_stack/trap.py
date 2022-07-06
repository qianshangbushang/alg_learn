#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :trap.py
# @Time      :2022/7/6 10:45


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        42. https://leetcode.cn/problems/trapping-rain-water/
        :param height:
        :return:
        """

        result = 0
        stack = []
        for idx in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[idx]:
                if len(stack) > 1:
                    mid = height[stack[-1]]
                    left = height[stack[-2]]
                    right = height[idx]
                    h = min(left, right) - mid
                    result += h * (idx - stack[-2] - 1)
                stack.pop()
            stack.append(idx)
        return result

    def trap2(self, height: List[int]) -> int:
        """
        42. https://leetcode.cn/problems/trapping-rain-water/
        :param height:
        :return:
        """
        right = [0] * len(height)
        for idx in range(len(height) - 2, -1, -1):
            right[idx] = max(right[idx + 1], height[idx + 1])

        left = [0] * len(height)
        for idx in range(1, len(height)):
            left[idx] = max(left[idx - 1], height[idx - 1])

        result = 0
        for idx in range(1, len(height) - 1):
            min_h = min(left[idx], right[idx])
            if min_h < height[idx]:
                continue
            result += min_h - height[idx]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([4, 2, 0, 3, 2, 5]))

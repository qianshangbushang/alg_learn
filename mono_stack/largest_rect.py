#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :largest_rect.py
# @Time      :2022/7/6 11:44


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        84. https://leetcode.cn/problems/largest-rectangle-in-histogram/

        :param heights:
        :return:
        """
        result = 0
        stack = [0]
        new_data = [0] + heights + [0]

        for idx in range(1, len(new_data)):
            while len(stack) > 0 and new_data[stack[-1]] > new_data[idx]:
                right = idx
                mid = stack[-1]
                left = stack[-2]
                w = right - left - 1
                h = new_data[mid]
                result = max(result, w * h)
                stack.pop()
            stack.append(idx)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))

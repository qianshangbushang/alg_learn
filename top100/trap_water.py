#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :trap_water.py
# @Time      :2022/7/13 10:52


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈思路

        单调递减栈，碰到无法入栈元素，开始收割之前的结果
        :param height:
        :return:
        """
        arr = []
        result = 0

        height = [0] + height + [0]
        arr = [0]
        for idx in range(1, len(height)):
            curr_h = height[idx]
            last_h = height[arr[-1]]
            if last_h > curr_h:
                arr.append(idx)
                continue

            if last_h == curr_h:
                arr.pop()
                arr.append(idx)
                continue

            while last_h < curr_h and len(arr) > 1:
                mid_height = height[arr.pop()]
                left_height = height[arr[-1]]

                h = min(curr_h, left_height) - mid_height
                w = idx - arr[-1] - 1
                s = max(h, 0) * w
                print(s, h, w)
                result += s
                last_h = left_height
            arr.append(idx)
        return result

    def trap1(self, height: List[int]) -> int:
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
    # print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))

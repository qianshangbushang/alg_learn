#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :daily_temperature.py
# @Time      :2022/7/6 10:12


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        739. https://leetcode.cn/problems/daily-temperatures/

        :param temperatures:
        :return:
        """
        stack = []
        result = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            # if len(stack) == 0 or temperatures[idx] <= temperatures[stack[-1]]:
            #     stack.append(idx)
            #     continue
            while len(stack) > 0 and temperatures[idx] > temperatures[stack[-1]]:
                result[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

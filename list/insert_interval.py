#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :insert_interval.py
# @Time      :2022/10/27 17:47


from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result, idx = [], 0

        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx += 1

        if idx == len(intervals):
            result.append(newInterval)
            return result
        temp = [newInterval[0], newInterval[1]]
        while idx < len(intervals) and intervals[idx][0] <= temp[1]:
            temp[0] = min(intervals[idx][0], temp[0])
            temp[1] = max(intervals[idx][1], temp[1])
            idx += 1
        result.append(temp)

        while idx < len(intervals):
            result.append(intervals[idx])
            idx += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(s.insert([], [5, 7]))
    print(s.insert([[1, 5]], [2, 7]))
    print(s.insert([[1, 5]], [6, 8]))
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
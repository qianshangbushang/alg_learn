#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :erase_overlap.py
# @Time      :2022/7/1 14:09


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])

        point_cnt = 1
        min_right = intervals[0][1]
        for x in intervals:
            if min_right > x[0]:
                continue
            point_cnt += 1
            min_right = x[1]
        return len(intervals) - point_cnt


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))

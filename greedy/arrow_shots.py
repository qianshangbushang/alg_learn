#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :arrow_shots.py
# @Time      :2022/7/1 13:18


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        arrow_cnt = 1
        min_edge = points[0][1]
        for p in points:
            if min_edge >= p[0]:
                min_edge = min(min_edge, p[1])
                continue

            arrow_cnt += 1
            min_edge = p[1]
        return arrow_cnt


if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))

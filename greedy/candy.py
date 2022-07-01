#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :candy.py
# @Time      :2022/7/1 11:23


from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ret = [1] * len(ratings)
        idx = 1
        while idx < len(ratings):
            if ratings[idx] > ratings[idx - 1]:
                ret[idx] = ret[idx - 1] + 1
            idx += 1
        idx -= 2
        while idx >= 0:
            if ratings[idx] > ratings[idx + 1] and ret[idx] <= ret[idx + 1]:
                ret[idx] = ret[idx + 1] + 1
            idx -= 1
        return sum(ret)


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 3, 4, 5, 2]))

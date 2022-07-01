#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gas_station.py
# @Time      :2022/7/1 10:24


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(left) < 0:
            return -1

        cur_sum = 0
        cur_idx = 0
        for idx, val in enumerate(left):
            if cur_sum < 0:
                cur_sum = val
                cur_idx = idx
                continue
            cur_sum += val
        return cur_idx

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        left = []
        min_sum = None
        cur_sum = 0
        for i in range(len(gas)):
            left.append(gas[i] - cost[i])
            cur_sum += left[i]
            if not min_sum or min_sum > cur_sum:
                min_sum = cur_sum

        if cur_sum < 0:
            return -1
        if min_sum > 0:
            return 0

        idx = len(gas) - 1
        while idx > 0:
            min_sum += left[idx]
            if min_sum >= 0:
                break
            idx -= 1
        return idx


if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))

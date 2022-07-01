#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lemon_change.py
# @Time      :2022/7/1 11:38


from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = defaultdict(int)
        for x in bills:
            if x == 5:
                counter[5] += 1
            if x == 10:
                counter[10] += 1
                if counter[5] <= 0:
                    return False
                counter[5] -= 1
            if x == 20:
                if counter[5] <= 0:
                    return False
                if counter[10] >= 1:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.lemonadeChange([5, 5, 5, 10, 20]))
    print(s.lemonadeChange([5, 5, 10, 20]))
    print(s.lemonadeChange([5, 10, 20]))

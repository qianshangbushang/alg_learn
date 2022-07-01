#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :restruct_height.py
# @Time      :2022/7/1 11:54


from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        ret = []

        for x in people:
            ret.insert(x[1], x)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

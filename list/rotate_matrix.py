#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :rotate_matrix.py
# @Time      :2022/10/27 15:13


from typing import List


class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        n = len(a)
        for row in range(len(a) // 2):
            # 起始点 a[m][m]
            for col in range(row, n - 1 - row):
                tmp = a[row][col]
                a[row][col] = a[n - 1 - col][row]
                a[n - 1 - col][row] = a[n - 1 - row][n - 1 - col]
                a[n - 1 - row][n - 1 - col] = a[col][n - 1 - row]
                a[col][n - 1 - row] = tmp
        return


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

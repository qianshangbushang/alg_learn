#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :spiral_matrix.py
# @Time      :2022/7/12 10:07


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        h_start, h_end = 0, len(matrix[0]) - 1  # 闭区间
        v_start, v_end = 0, len(matrix) - 1

        result = []

        while h_start < h_end and v_start < v_end:
            h_idx = h_start
            v_idx = v_start
            while h_idx < h_end:
                cur_val = matrix[v_idx][h_idx]
                result.append(cur_val)
                h_idx += 1

            while v_idx < v_end:
                cur_val = matrix[v_idx][h_idx]
                result.append(cur_val)
                v_idx += 1

            while h_idx > h_start:
                cur_val = matrix[v_idx][h_idx]
                result.append(cur_val)
                h_idx -= 1

            while v_idx > v_start:
                cur_val = matrix[v_idx][h_idx]
                result.append(cur_val)
                v_idx -= 1

            h_start += 1
            v_start += 1
            v_end -= 1
            h_end -= 1

        if h_start == h_end and v_start == v_end:
            result.append(matrix[v_end][h_end])

        if h_start == h_end and v_start != v_end:
            result.extend([matrix[v][h_start] for v in range(v_start, v_end + 1)])

        if h_start != h_end and v_start == v_end:
            result.extend([matrix[v_end][h] for h in range(h_start, h_end + 1)])

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(s.spiralOrder([[6, 9, 7]]))
    print(s.spiralOrder([[2, 5], [8, 4], [0, -1]]))

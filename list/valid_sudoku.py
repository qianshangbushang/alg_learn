#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :valid_sudoku.py
# @Time      :2022/10/27 14:30


from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_dict[i]:
                    return False
                else:
                    row_dict[i].add(board[i][j])

                if board[i][j] in col_dict[j]:
                    return False
                else:
                    col_dict[j].add(board[i][j])

                if board[i][j] in box_dict[i // 3 * 3 + j // 3]:
                    return False
                else:
                    box_dict[i // 3 * 3 + j // 3].add(board[i][j])
        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:

        def check_valid(data: List[str]):
            exist = set()
            for x in data:
                if x in exist and x != '.':
                    return False
                else:
                    exist.add(x)
            return True

        def cond1_valid(board: List[List[str]]):
            for l in board:
                print(f"L: {l}")
                if not check_valid(l):
                    return False
            return True

        def cond2_valid(board: List[List[str]]):
            for c in zip(*board):
                if not check_valid(c):
                    return False
            return True

        def cond3_valid(board: List[List[str]]):
            for i in range(3):
                for j in range(3):
                    m = [board[i * 3 + x][j * 3 + y] for x in range(3) for y in range(3)]
                    if not check_valid(m):
                        return False
            return True

        return cond1_valid(board) and cond2_valid(board) and cond3_valid(board)


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s = Solution()
    print(s.isValidSudoku(board))

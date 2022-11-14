#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :surrounded_region.py
# @Time      :2022/11/11 15:24


from typing import List, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i not in [0, len(board) - 1]) and (j not in [0, len(board[0]) - 1]):
                    continue
                if board[i][j] != "O":
                    continue
                self.modify((i, j), board, 'A')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                    continue

                if board[i][j] == 'O':
                    board[i][j] = 'X'
        return

    def is_valid(self, point: Tuple[int, int], board):
        cond1 = 0 <= point[0] < len(board)
        cond2 = 0 <= point[1] < len(board[0])
        return cond1 and cond2

    def modify(self, point: Tuple[int, int], board, key='A'):
        if not self.is_valid(point, board):
            return
        if board[point[0]][point[1]] in ['X', key]:
            return
        board[point[0]][point[1]] = key
        for direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            new_point = (point[0] + direction[0], point[1] + direction[1])
            self.modify(new_point, board)
        return


if __name__ == '__main__':
    s = Solution()
    arr = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(arr)
    print(*arr, sep='\n')

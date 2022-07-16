#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :maze.py
# @Time      :2022/7/15 21:30


import sys


def run():
    sys.stdin.readline()
    lines = [[int(m) for m in x.strip().split(' ')] for x in sys.stdin.readlines()]
    logic(lines)
    return


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        # self.x -= 1
        return point(self.x, self.y - 1)

    def move_right(self):
        return point(self.x, self.y + 1)

    def move_down(self):
        return point(self.x + 1, self.y)

    def move_up(self):
        return point(self.x - 1, self.y)

    def next_choice_list(self):
        return [
            self.move_left(),
            self.move_right(),
            self.move_down(),
            self.move_up(),
        ]

    def in_map(self, data):
        cond1 = self.x < len(data) and self.y < len(data[0])
        cond2 = self.x >= 0 and self.y >= 0
        return cond1 and cond2

    def is_same(self, p):
        if not p:
            return False
        return self.x == p.x and self.y == p.y


def logic(data):
    end_point = point(len(data[0]) - 1, len(data) - 1)

    # print(end_point.x, end_point.y)
    def dfs(path):
        curr_point = path[-1]  # 0-> x坐标， 1->y坐标
        if len(path) == 1:
            last_point = None
        else:
            last_point = path[-2]

        print(curr_point.x, curr_point.y)
        if curr_point.is_same(end_point):
            for x in path:
                print(f"({x.x},{x.y})")
            return True

        # print(f"path size: {len(path)}")
        for next_point in curr_point.next_choice_list():
            print(next_point.x, next_point.y)
            if not next_point.in_map(data):
                print("not in map")
                continue
            if next_point.is_same(last_point):
                print("same to last point")
                continue
            if data[next_point.x][next_point.y] == 1:
                print("encounted wall")
                continue

            path.append(next_point)
            if dfs(path):
                return True
            path.pop()
        return False

    dfs([point(0, 0)])
    return


run()

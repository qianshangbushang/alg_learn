#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p1563.py
# @Time      :2022/10/25 15:09


class Person(object):
    def __init__(self, idx, dir, name):
        self.idx = idx
        self.dir = dir
        self.name = name

    """
    面朝圈内的玩具小人, 它的左边是顺时针方向, 右边是逆时针方向; 而面向圈外的玩具小人, 它的左边是逆时针方向, 右边是顺时针方向
    """

    def left(self, idx_delta):
        if self.dir == 0:  # 朝向圈内
            return self.idx - idx_delta
        else:
            return self.idx + idx_delta

    def right(self, idx_delta):
        if self.dir == 0:
            return self.idx + idx_delta
        else:
            return self.idx - idx_delta


def run():
    n, m = map(int, input().split())
    person_list = []
    for i in range(n):
        dir, name = input().split()
        person_list.append(Person(i, int(dir), name))

    curr_p = person_list[0]
    for i in range(m):
        is_right, step = map(int, input().split())
        if is_right:
            next_p_id = curr_p.right(step)
        else:
            next_p_id = curr_p.left(step)

        # relocation
        while next_p_id < 0:
            next_p_id += len(person_list)
        if next_p_id >= len(person_list):
            next_p_id = next_p_id % len(person_list)

        curr_p = person_list[next_p_id]
    print(curr_p.name)


if __name__ == '__main__':
    run()

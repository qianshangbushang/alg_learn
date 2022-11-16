#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :course_schedule.py
# @Time      :2022/11/14 16:38


from collections import defaultdict, deque
from typing import List


class Course(object):
    def __init__(self, course_id):
        self.course_id = course_id
        self.next_courses = []
        self.indegree = 0


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        ind = [0] * numCourses
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            ind[pair[0]] += 1

        que = deque()
        for i, v in enumerate(ind):
            if v == 0:
                que.append(i)
        visited = set()
        while len(que) > 0:
            curr = que.popleft()
            if curr in visited:
                return False
            visited.add(curr)
            for nxt in adj[curr]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    que.append(nxt)
        return len(visited) == numCourses

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = defaultdict()
        for course1, course2 in prerequisites:
            if course2 not in course_dict:
                course_dict[course2] = Course(course2)
            if course1 not in course_dict:
                course_dict[course1] = Course(course1)

            # course1 依赖 course2
            course_dict[course1].indegree += 1
            course_dict[course2].next_courses.append(course1)

        course_queue = deque()

        for course_id, course in course_dict.items():
            if course.indegree == 0:
                course_queue.append(course_id)
        count = len(course_dict)
        while len(course_queue) > 0:
            curr_id = course_queue.popleft()
            for next_id in course_dict[curr_id].next_courses:
                course_dict[next_id].indegree -= 1
                if course_dict[next_id].indegree == 0:
                    course_queue.append(next_id)
            count -= 1

        return count == 0


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0], [0, 1]]))
    print(s.canFinish(2, [[1, 0]]))
    print(s.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))

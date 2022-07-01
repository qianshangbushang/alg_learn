from typing import List

from black import main


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])

        result = []
        item = None
        for x in intervals:
            if not item:
                item = [x[0], x[1]]
                continue

            if item[1] >= x[0]:
                item[1] = max(x[1], item[1])
                continue

            result.append(item)
            item = [x[0], x[1]]

        result.append(item)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [4, 6]]))

# 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，
# 并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。
# 这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。
# 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。
#
import random
from typing import List



def quicksort(arr:List[int]):
    reorder(arr, 0, len(arr) - 1)
    return

def reorder(arr:List[int], start:int, end:int):
    if start >= end:
        return
    left, right, pivot =start, end,  random.randint(start, end)
    arr[pivot], arr[end] = arr[end], arr[pivot]
    
    pivot = arr[pivot]
    while left < right:
        while left < right and arr[right] >  pivot:
            right -= 1
            continue
        
        

        while left > right and arr[right] > pivot:
            right -= 1
            continue

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1
    arr[left], arr[end] = arr[end], arr[left]
    print(arr[left], arr)
    reorder(arr, start, left - 1)
    reorder(arr, left + 1, end)
    return


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[1] * x[1] + x[0] * x[0])
        return points[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.reorder(points, 0, len(points) - 1, k)
        return points[:k]

    def reorder(self, points, start, end, k):
        pivot = random.randint(start, end)
        pp = points[pivot]
        points[end], points[pivot] = points[pivot], points[end]
        left, right = start, end - 1
        while left < right:
            print(pp)
            lp, rp = points[left], points[right]

            # 找到左边第一个大于标志位的
            if left < right and self.squreDist(lp) < self.squreDist(pp):
                left += 1
                continue

            # 找到右边第一个小于标志位的
            if left < right and self.squreDist(rp) > self.squreDist(pp):
                right -= 1
                continue
           # 交换
            points[left], points[right] = points[right], points[left]
            left += 1
            right -= 1

        points[left], points[end]= points[end], points[left]
        print(start, left, end)

        if left < k - 1:
            return self.reorder(points, left + 1, end, k)
        elif left > k - 1:
            return self.reorder(points, start, left , k)
        

    def squreDist(self, p: List[int]):
        return p[0] * p[0] + p[1] * p[1]


if __name__ == "__main__":
    s = Solution()
    # print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
    # print(s.kClosest(points=[[0, 1], [1, 0]], k=2))
    # print(s.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3))
    arr = [15, 46, 55, 82, 86, 96, 36, 51, 9, 89]
    print(quicksort(arr))
    print(arr)
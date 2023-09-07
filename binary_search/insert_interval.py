# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 示例 1：
# 
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
# 
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。


from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result, i=[], 0
        while i < len(intervals):
            item = intervals[i]
            if self.is_after(newInterval, item):
                result.append(item)
                i += 1
                continue
            
            if self.is_before(newInterval, item):
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            
            if self.has_overlap(newInterval, item):
                newInterval = [min(newInterval[0], item[0]), max(newInterval[1], item[1])]
                i += 1
                continue
        result.append(newInterval)
        return result

    def is_before(self, x:List[int], y:List[int]):
        return x[1] <  y[0]
    
    def is_after(self, x:List[int], y:List[int]):
        return x[0] >  y[1]
    
    def has_overlap(self, x:List[int], y:List[int]):
        return max(x[0], y[0]) <= min(x[1], y[1])


if __name__ == "__main__":
    s = Solution()
    print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
    print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
    print(s.insert(intervals = [[1,5]], newInterval = [2,3]))
    print(s.insert(intervals = [], newInterval = [2,3]))
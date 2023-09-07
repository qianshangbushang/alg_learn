# 给你一个整数数组 ranks ，表示一些机械工的 能力值 。
# ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。
#
# 同时给你一个整数 cars ，表示总共需要修理的汽车数目。
#
# 请你返回修理所有汽车 最少 需要多少时间。
#
# 注意：所有机械工可以同时修理汽车。
#
#
#
# 示例 1：
#
# 输入：ranks = [4,2,3,1], cars = 10
# 输出：16
# 解释：
# - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
# - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
# - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
# - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# 16 分钟是修理完所有车需要的最少时间。


from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l_time, r_time =0, min(ranks) * cars * cars

        while l_time < r_time:
            mid_time = l_time + (r_time - l_time) // 2
            car_repaired = sum([int(math.sqrt(mid_time/r)) for r in ranks])

            if car_repaired < cars:
                l_time = mid_time + 1
            else:
                r_time = mid_time - 1
        return l_time

# class Solution:
#     def repairCars(self, ranks: List[int], cars: int) -> int:
#         result_val = None
#         def backtrack(nth_worker, left_cars, cost_list: List[int]):
#             nonlocal result_val
#             if nth_worker == len(ranks):
#                 max_cost =  max(cost_list + [ranks[nth_worker - 1] * left_cars * left_cars])
#                 result_val = min(result_val, max_cost) if result_val else max_cost
#                 return
# 
#             for x in range(left_cars):
#                 curr_cost = ranks[nth_worker - 1] * x * x
#                 backtrack(nth_worker + 1, left_cars - x, cost_list + [curr_cost])
#             return
# 
#         backtrack(1, cars, [])
#         return result_val
    

if __name__ == "__main__":
    s = Solution()
    print(s.repairCars([4, 2, 3, 1], 10))
    print(s.repairCars([5, 1, 8], 6))

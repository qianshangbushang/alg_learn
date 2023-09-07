# 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，
# 表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，
# 你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，
# 并返回该价格。 如果不存在这样的路线，则输出 -1。
#
# 示例 1：
#
# 输入:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200


from typing import List
from collections import defaultdict


class Solution:
    min_cost = None
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def backtrack(curr_node: int, pass_k_station: int, cost: int, next_flight, path: set):
            if curr_node == dst:
                self.min_cost = min(cost, self.min_cost) if self.min_cost else cost
                return
            if pass_k_station > k:
                return
            for f in next_flight[curr_node]:
                # 已经经过的节点
                if f[1] in path:
                    continue
                path.add(f[1])
                backtrack(f[1], pass_k_station+1, cost + f[2],  next_flight, path)
                path.remove(f[1])
                print(path)
            return

        # 记录后续可以选择的航班
        next_flight = defaultdict(list)
        for f in flights:
            next_flight[f[0]].append(f)

        backtrack(src, 0, 0, next_flight, set())
        return self.min_cost if self.min_cost else -1

class Solution:
    min_cost = None
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        next_flight = defaultdict(list)
        for f in flights:
            next_flight[f[0]].append(f)

        dp = [None] * n
        dp[src] = 0

        for f in next_flight[src]:
            dp[f[1]] = min(dp[f[1]], dp[src] + f[2]) if dp[f] else f[2]
        


        return

if __name__ == "__main__":
    s = Solution()
    print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
    s = Solution()
    print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
    s = Solution()
    print(s.findCheapestPrice(n=17, flights=[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]], src=13, dst=4, k=13))
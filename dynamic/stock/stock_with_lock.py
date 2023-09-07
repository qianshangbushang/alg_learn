# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 买入，卖出，冷冻
        a, b, c = -prices[0], 0, 0

        for p in prices[1:]:
            # 买入 上一个阶段必须是冷冻
            a = max(a, c - p)
            # 冷冻 上一个阶段必须是卖出, 当天不能冷冻， 必须再卖出之前算
            c = max(c, b)
            # 卖出，上一个阶段必须是买入
            b = max(b, a + p)

        return max(b, c)
    

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))

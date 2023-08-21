###################################################
# 给你一个整数数组 cookies ，其中 cookies[i] 表示在第 i 个零食包中的饼干数量。另给你一个整数 k 表示等待分发零食包的孩子数量，
# 所有 零食包都需要分发。在同一个零食包中的所有饼干都必须分发给同一个孩子，不能分开。
# 分发的 不公平程度 定义为单个孩子在分发过程中能够获得饼干的最大总数。
# 返回所有分发的最小不公平程度
# case1
#     输入：cookies = [8,15,10,20,8], k = 2
#     输出：31
#     解释：一种最优方案是 [8,15,8] 和 [10,20] 。
#     - 第 1 个孩子分到 [8,15,8] ，总计 8 + 15 + 8 = 31 块饼干。
#     - 第 2 个孩子分到 [10,20] ，总计 10 + 20 = 30 块饼干。
#     分发的不公平程度为 max(31,30) = 31 。
#     可以证明不存在不公平程度小于 31 的分发方案。
#
# case2
#    输入：cookies = [6,1,3,2,2,4,1,2], k = 3
#    输出：7
#    解释：一种最优方案是 [6,1]、[3,2,2] 和 [4,1,2] 。
#    - 第 1 个孩子分到 [6,1] ，总计 6 + 1 = 7 块饼干。
#    - 第 2 个孩子分到 [3,2,2] ，总计 3 + 2 + 2 = 7 块饼干。
#    - 第 3 个孩子分到 [4,1,2] ，总计 4 + 1 + 2 = 7 块饼干。
#    分发的不公平程度为 max(7,7,7) = 7 。
#    可以证明不存在不公平程度小于 7 的分发方案。

###################################################


from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort()
        def backtrack(left_cookies: List[int], distribute_list: List[int]):
            print(left_cookies, distribute_list)
            if len(left_cookies) == 0:
                return max(distribute_list)
            result = None
            for i in range(len(left_cookies)):
                if i >= 1 and  left_cookies[i] == left_cookies[i-1]:
                    continue
                for j in range(k):
                    if result and any([x > result for x in distribute_list]):
                        continue
                    if distribute_list[j] in distribute_list[:j]:
                        continue
                    
                    distribute_list[j] += left_cookies[i]
                    curr = backtrack(left_cookies[:i] + left_cookies[i+1:], distribute_list)
                    result = curr if not result or curr < result else result
                    distribute_list[j] -= left_cookies[i]
            return result
        return backtrack(cookies, [0] * k)


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCookies(cookies=[6, 1, 3, 4, 1, 2], k=3))
    # print(s.distributeCookies(cookies = [8,15,10,20,8], k = 2))
    # print(s.distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3))

from typing import List

# 1 0 -1
# 1 1 0
#

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        existed_dict = {0: 1}
        cur_sum = result = 0
        for x in nums:
            cur_sum += x
            result += existed_dict.get(cur_sum - k, 0)
            existed_dict[cur_sum] = existed_dict.get(cur_sum, 0) + 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1, 0, -1], 0))

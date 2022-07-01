from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = delta = 0
        delta_dict = {0: -1}
        for idx, x in enumerate(nums):
            delta += 1 if x == 1 else -1
            last_idx = delta_dict.get(delta, None)
            print(idx, delta, delta_dict)
            if last_idx is not None:
                max_len = max(idx - last_idx, max_len)
            if delta not in delta_dict:
                delta_dict[delta] = idx
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength([0, 1, 0, 1]))

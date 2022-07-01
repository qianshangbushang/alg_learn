from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = dict([(ch, idx) for idx, ch in enumerate(order)])
        print(order_dict)

        for idx in range(max([len(x) for x in words])):
            for idy in range(1, len(words)):
                last_order = order_dict[words[idy - 1][idx]] if idx < len(words[idy - 1]) else 0
                curr_order = order_dict[words[idy][idx]] if idx < len(words[idy]) else 0
                if last_order == curr_order:
                    continue
                if curr_order < last_order:
                    print(last_order, curr_order, words[idy - 1][idx], words[idy][idx])
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))

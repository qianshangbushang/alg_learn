# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 注意：本题中，每个活字字模只能使用一次。
#
# 示例 1：
#
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 示例 2：
#
# 输入："AAABBC"
# 输出：188
#
from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(cur_path: str, used: List[int]):
            if all(used):
                return 0
            skip = set()
            result = 0
            for i in range(0, len(tiles)):
                if used[i]:
                    continue
                if tiles[i] in skip:
                    continue
                skip.add(tiles[i])
                # 和上一个相同，跳过
                used[i] = True
                result += 1
                result += backtrack(cur_path + tiles[i], used)
                used[i] = False
            return result

        return backtrack("", [False] * len(tiles))


if __name__ == "__main__":
    s = Solution()
    print(s.numTilePossibilities("AAB"))

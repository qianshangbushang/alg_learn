class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        r = [1] * 2 + [0] * (n - 1)
        for i in range(2, n + 1):
            for j in range(0, i):
                r[i] += r[j] * r[i - j - 1]
        return r[-1]

    def _num_tree(self, start: int, end: int):
        if start == end:
            return 1

        num = 0
        for x in range(start, end):
            # x 作为根节点，小于x作为左子树, 大于 x 作为右子树
            num += self._num_tree(start, x) * self._num_tree(x + 1, end)
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(8))

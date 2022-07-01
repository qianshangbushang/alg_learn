from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        def _compute_code(s: str):
            x = [0] * 26
            for ch in s:
                x[ord(ch) - ord("a")] += 1
            return "|".join([str(m) for m in x])

        for x in strs:
            code_x = _compute_code(x)
            print(code_x)
            if code_x not in anagram_map:
                anagram_map[code_x] = []
            anagram_map[code_x].append(x)
        print(anagram_map)
        return list(anagram_map.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))

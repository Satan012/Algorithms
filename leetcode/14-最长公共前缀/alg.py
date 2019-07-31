class Solution:
    def LCP(self, s1, s2):
        if s1 is None or s2 is None or len(s1) == 0 or len(s2) == 0:
            return ''
        else:
            length = len(s2) if len(s1) >= len(s2) else len(s1)
            for i in range(length):
                if s1[i] != s2[i]:
                    return s1[:i]
            return s1[:i + 1]

    def getLongestCommonPrefix(self, strs, start, end):
        if start == end:
            return strs[start]
        else:
            mid = (start + end) // 2
            leftLCP = self.getLongestCommonPrefix(strs, start, mid)
            rightLCP = self.getLongestCommonPrefix(strs, mid + 1, end)
            final_LCP = self.LCP(leftLCP, rightLCP)
            return final_LCP

    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ''
        return self.getLongestCommonPrefix(strs, 0, len(strs) - 1)


if __name__ == '__main__':
    solution = Solution()
    strs = []

    print(solution.longestCommonPrefix(strs))

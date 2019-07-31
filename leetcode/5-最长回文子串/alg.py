class Solution:
    def longestPalindrome(self, s):
        """
        时间复杂度O(N^2)
        :param s:
        :return:
        """
        length = len(s)
        if length <= 1:
            return s

        longest_l = 1
        res = s[0]

        dp = [[False] * length for _ in range(length)]

        for r in range(1, length):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1] is True):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l: r + 1]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("aaaa"))

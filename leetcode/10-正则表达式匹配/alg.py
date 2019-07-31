class Solution(object):
    def isMatch(self, text, pattern):  # 回溯
        if not pattern:  # 如果text为0但是pattern不为0是需要进一步判断的，所以线判断pattern比较好
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}  # 如果text不为0且第一个匹配上了

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatch_2(self, text, pattern):  # 自底向上的动态规划  O(TN)
        len_t = len(text)
        len_p = len(pattern)
        dp = [[False] * (len_p + 1) for _ in range(len_t + 1)]

        dp[-1][-1] = True
        for i in range(len_t, -1, -1):
            for j in range(len_p - 1, -1, -1):
                first_match = i < len_t and pattern[j] in {text[i], '.'}

                if j + 1 < len_p and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


if __name__ == '__main__':
    soulution = Solution()

    s = 'aa'
    p = '*'

    print(soulution.isMatch(s, p))

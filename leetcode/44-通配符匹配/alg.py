class Solution:
    def isMatch(self, s, p):
        length_s = len(s)
        length_p = len(p)

        dp = [[False] * (length_p + 1) for _ in range(length_s + 1)]

        dp[-1][-1] = True

        for i in range(length_s, -1, -1):
            for j in range(length_p - 1, -1, -1):
                firstMatch = i < length_s and p[j] in [s[i], '?']

                if p[j] == '*':
                    dp[i][j] = dp[i][j + 1] or (i < length_s and dp[i + 1][j])
                else:
                    dp[i][j] = firstMatch and dp[i + 1][j + 1]

                # print(s[i:], p[j:], dp[i][j])
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()

    s = "acdcb"
    p = "a*c?b"

    print(solution.isMatch(s, p))

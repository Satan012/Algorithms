class Solution:
    def numDistinct(self, s, t):
        l_s = len(s)
        l_t = len(t)

        dp = [[0] * (l_t + 1) for _ in range(l_s + 1)]

        for i in range(l_s):
            dp[i][0] = 1

        for i in range(1, l_s + 1):
            for j in range(1, l_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    S = "babgbag"
    T = "bag"

    print(solution.numDistinct(S, T))

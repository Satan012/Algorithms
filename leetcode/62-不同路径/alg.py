class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]  # m*n
        dp[-1][-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                down_paths = 0
                right_paths = 0

                flag = False
                if i < m - 1:
                    flag = True
                    down_paths = dp[i + 1][j]
                if j < n - 1:
                    flag = True
                    right_paths = dp[i][j + 1]
                if flag:
                    dp[i][j] = down_paths + right_paths
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()

    m = 7
    n = 3

    print(solution.uniquePaths(m, n))

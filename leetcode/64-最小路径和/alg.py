# class Solution:
#     def minPathSum(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#
#         dp = [[0] * n for _ in range(m)]  # dp[i][j]表示从i,j到终点的最小路径和
#         dp[-1][-1] = grid[-1][-1]
#
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 down_min = -1
#                 right_min = -1
#
#                 if i + 1 < m:
#                     down_min = grid[i][j] + dp[i + 1][j]
#                 if j + 1 < n:
#                     right_min = grid[i][j] + dp[i][j + 1]
#
#                 if down_min * right_min < 0:
#                     dp[i][j] = max([down_min, right_min])
#                 else:
#                     if min([down_min, right_min]) != -1:
#                         dp[i][j] = min([down_min, right_min])
#
#         return dp[0][0]


class Solution:
    def minPathSum(self, grid):
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    x = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    print(solution.minPathSum(x))

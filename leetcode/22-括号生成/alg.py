class Solution(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(s='', left=0, right=0):
            print(s)
            if len(s) == 2 * N:
                ans.append(s)
                return
            if left < N:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans


if __name__ == '__main__':
    solution = Solution()

    n = 3

    print(solution.generateParenthesis(n))

class Solution:  # 现在理解的，回溯就是递归，动态规划不是递归貌似
    def backtrack(self, phone, digits, cur_idx, results, seq):
        if cur_idx == len(digits):
            results.append(seq)
            return

        for i in range(len(phone[digits[cur_idx]])):
            self.backtrack(phone, digits, cur_idx + 1, results, seq + phone[digits[cur_idx]][i])

    def letterCombinations(self, digits):
        if digits is None or len(digits) == 0:
            return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        results = []

        self.backtrack(phone, digits, cur_idx=0, results=results, seq='')

        return results


if __name__ == '__main__':
    solution = Solution()

    digits = '246'

    print(solution.letterCombinations(digits))

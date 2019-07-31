class Solution:
    def intToRoman(self, num):
        table = {
            1: {1: 'I', 5: 'V'},
            10: {1: 'X', 5: 'L'},
            100: {1: 'C', 5: 'D'},
            1000: {1: 'M'}
        }
        result = ''
        x = 1
        while num != 0:
            pop = int(num % 10)
            if pop != 0:
                tmp = pop % 5
                if pop == 9:
                    result = table[x][1] + table[x * 10][1] + result
                elif 5 <= pop < 9:
                    result = table[x][5] + table[x][1] * tmp + result
                elif pop == 4:
                    result = table[x][1] + table[x][5] + result
                else:
                    result = table[x][1] * tmp + result
            num = num // 10
            x *= 10
        return result


if __name__ == '__main__':
    solution = Solution()

    num = 3999

    print(solution.intToRoman(num))

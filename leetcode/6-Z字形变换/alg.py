class Solution:
    def convert(self, s, numRows):
        length_s = len(s)

        results = ['a' for _ in range(length_s)]
        result_indx = -1

        if length_s < 2 or numRows == 1:
            return s

        stride_down = (numRows - 1) * 2
        start_idx = 0
        while start_idx < length_s:  # 为了减少循环判断，把头和为尾单独拿出

            result_indx += 1
            print(start_idx, result_indx)
            results[result_indx] = s[start_idx]
            start_idx += stride_down

        for row in range(numRows - 1, 1, -1):
            stride_down = (row - 1) * 2
            stride_up = (numRows - row) * 2

            if row == numRows:
                stride_up = stride_down
            if row == 1:
                stride_down = stride_up

            start_idx = numRows - row
            count = 1
            while start_idx < length_s:
                result_indx += 1
                results[result_indx] = s[start_idx]
                if count % 2 == 1:
                    start_idx += stride_down
                else:
                    start_idx += stride_up
                count += 1

        stride_up = (numRows - 1) * 2
        start_idx = numRows - 1
        while start_idx < length_s:
            result_indx += 1
            results[result_indx] = s[start_idx]
            start_idx += stride_up

        return ''.join(results)


if __name__ == '__main__':
    solution = Solution()
    s = "LEETCODEISHIRING"
    print(solution.convert('A', 1))

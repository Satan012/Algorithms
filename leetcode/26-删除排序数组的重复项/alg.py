class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)

        if length == 0:
            return 0

        cur_index = 0

        for i in range(1, length):
            if nums[i] != nums[cur_index]:
                cur_index += 1
                nums[cur_index] = nums[i]

        return cur_index + 1


if __name__ == '__main__':
    solution = Solution()
    nums = []
    print(solution.removeDuplicates(nums))
    print(nums)

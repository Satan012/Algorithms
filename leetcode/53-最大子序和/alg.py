class Solution:
    def maxSubArray(self, nums):
        i = j = 0
        maxSum = nums[0]  # 假设nums[0]是最大的sum值

        while j < len(nums):
            cur_sum = sum(nums[i: j + 1])
            if cur_sum > maxSum:
                maxSum = cur_sum

            if j < len(nums) - 1 and cur_sum + nums[j + 1] < nums[j + 1]:
                i = j = j + 1
            else:
                j += 1
        return maxSum

    def maxSubArray_2(self, nums):  # 分治, 三种情况，最大序列在左边，最大序列在右边，最大序列横跨两个部分，O(nlogn)
        def divide(left, right, nums):
            if left == right:
                return nums[left]
            center = (left + right) // 2

            leftMax = divide(left, center, nums)  # 最大字序列在最左部
            rightMax = divide(center + 1, right, nums)  # 最大字序列在右部

            leftBounderSum = nums[center]
            leftSum = nums[center]
            for i in range(center - 1, left - 1, -1):
                leftSum += nums[i]
                if leftSum > leftBounderSum:
                    leftBounderSum = leftSum

            rightBounderSum = nums[center + 1]
            rightSum = nums[center + 1]
            for j in range(center + 2, right + 1):
                rightSum += nums[j]
                if rightSum > rightBounderSum:
                    rightBounderSum = rightSum

            bounderMax = leftBounderSum + rightBounderSum

            return max([leftMax, rightMax, bounderMax])

        left = 0
        right = len(nums) - 1

        return divide(left, right, nums)


if __name__ == '__main__':
    solution = Solution()

    nums = [8, -19, 5, -4, 20]

    print(solution.maxSubArray_2(nums))

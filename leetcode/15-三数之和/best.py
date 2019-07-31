import bisect


class Solution:
    def threeSum(self, nums):
        ans = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        nums = sorted(counts)
        print(nums)
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -num * 2 in nums:
                        ans.append([num, num, -2 * num])
            if num < 0:
                twosum = -num
                left = bisect.bisect_left(nums, (twosum - nums[-1]), i + 1)
                for i in nums[left:bisect.bisect_right(nums, (twosum // 2), left)]:
                    j = twosum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])
        return ans


if __name__ == '__main__':
    solution = Solution()
    x = [-2, 0, 0, 2, 2]
    print(solution.threeSum(x))


# -*- coding:utf-8 -*-
from __future__ import division, print_function, absolute_import
import tensorflow as tf
import numpy as np


class Solution:
    def twoSum(self, nums, target):
        hasmap = {}
        for idx, n in enumerate(nums):
            another_idx = hasmap.setdefault(target-n, -1)
            if another_idx == -1:
                hasmap[n] = idx
            else:
                return [min([idx, another_idx]), max([idx, another_idx])]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))

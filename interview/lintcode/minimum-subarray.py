# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/9/5
# @Time: 16:21
# @url: http://www.lintcode.com/zh-cn/problem/minimum-subarray/
# @Description:给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        min_sum = min(nums)
        this_sum = 0
        for i in nums:
            this_sum += i
            if this_sum < min_sum:
                min_sum = this_sum
            if this_sum > 0:
                this_sum = 0
        return min_sum

if __name__ == '__main__':
    s = Solution()
    print (s.minSubArray([1, -1, -2, 1]))
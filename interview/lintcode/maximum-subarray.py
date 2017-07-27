# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/27
# @Time: 16:11
# @url: http://www.lintcode.com/zh-cn/problem/maximum-subarray/
# @Description:

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        max_sum = min(nums)
        this_sum = 0
        for i in nums:
            this_sum += i
            print (this_sum)
            if this_sum > max_sum:
                max_sum = this_sum
            if this_sum < 0:
                this_sum = 0
        return max_sum

if __name__ == '__main__':
    s = Solution()
    # print (s.maxSubArray([-2]))
    print (s.maxSubArray([-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000]))

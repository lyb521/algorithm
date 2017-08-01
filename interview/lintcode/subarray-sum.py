# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/1
# @Time: 21:42
# @url: http://www.lintcode.com/zh-cn/problem/subarray-sum/
# @Description:给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if len(nums) == 0:
            return False
        if len(nums) == 1 and sum(nums) == 0:
            return [0,0]
        for i in range(0, len(nums)-1):
            sums = nums[i]
            if sums == 0:
                return [i, i]
            for j in range(i + 1, len(nums)):
                sums += nums[j]
                if sums == 0:
                    return [i, j]
        return False


if __name__ == '__main__':
    s = Solution()
    print (s.subarraySum([0]))
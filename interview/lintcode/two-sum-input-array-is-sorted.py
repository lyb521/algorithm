# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/16
# @Time: 11:19
# @url: http://www.lintcode.com/zh-cn/problem/two-sum-input-array-is-sorted/
# @Description:给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。



class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # Write your code here
        for i in range(0, len(nums)):
            try:
                index2 = nums[i+1:].index(target - nums[i]) + i + 1
                if index2:
                    return [i+1, index2+1]
            except :
               pass
        return []


if __name__ == '__main__':
    s = Solution()
    print (s.twoSum([-1,0,1], 1))
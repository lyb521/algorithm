# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/7
# @Time: 15:04
# @url: http://www.lintcode.com/zh-cn/problem/majority-number/
# @Description:给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。。

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        main_total = 0
        main_num = 0
        for i in nums:
            count = nums.count(i)
            if count > main_total:
                main_total = count
                main_num = i
        return main_num

if __name__ == '__main__':
    s = Solution()
    print  s.majorityNumber([1,1,1,1,2,2,2])
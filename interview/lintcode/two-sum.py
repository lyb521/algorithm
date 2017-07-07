# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/7
# @Time: 10:47
# @url: http://www.lintcode.com/zh-cn/problem/two-sum/
# @Description:

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i in numbers:
            j = target - i
            if j in numbers:
                total = numbers.count(j)
                # 如果j和i相等，则必须存在两个一样的数
                if i == j and total < 2:
                    return  False
                else:
                    return [numbers.index(i) + 1,numbers.index(j, numbers.index(i)+1) + 1]
        return False

s = Solution()
print  s.twoSum([2,7,11,15], 9)
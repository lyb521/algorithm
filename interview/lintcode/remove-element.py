# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/10
# @Time: 17:14
# @url: http://www.lintcode.com/zh-cn/problem/remove-element/
# @Description:给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        if not A:
            return []
        for i in range(0, A.count(elem)):
            del A[A.index(elem)]
        return A


if __name__ == '__main__':
    s = Solution()
    print (s.removeElement([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))

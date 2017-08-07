# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/7
# @Time: 15:58
# @url: http://www.lintcode.com/zh-cn/problem/search-insert-position/
# @Description: 给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。你可以假设在数组中无重复元素。


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0
        for i in range(0, len(A)):
            if A[i] >= target:
                return i
        return len(A)


if __name__ == '__main__':
    s = Solution()
    print (s.searchInsert([0],1))
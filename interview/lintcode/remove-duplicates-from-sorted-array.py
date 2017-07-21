# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/10
# @Time: 18:37
# @url: http://www.lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-array/
# @Description: 给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。不要使用额外的数组空间，必须在原地没有额外空间的条件下完成


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        j = 0
        if not A:
            return 0
        for i in range(1, len(A)):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]
        A = A[0:j+1]
        return len(A)

if __name__ == '__main__':
    s = Solution()
    print (s.removeDuplicates([]))
    print (s.removeDuplicates([-14,-14,-13,-13,-13,-13,-13,-13,-13,-12,-12,-12,-12,-11,-10,-9,-9,-9,-8,-7,-5,-5,-5,-5,-4,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,14,14,14,14,15,16,16,16,18,18,18,19,19,19,19,20,20,20,21,21,21,21,21,21,22,22,22,22,22,23,23,24,25,25]))
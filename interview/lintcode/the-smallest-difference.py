# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/10/9
# @Time: 14:33
# @url: http://www.lintcode.com/zh-cn/problem/the-smallest-difference/
# @Description: 给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取 B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|)。返回最小差。
#
import sys

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        # write your code here
        A = sorted(A)
        B = sorted(B)
        res = sys.maxsize
        p1, p2 = 0, 0
        while p1 < len(A) and p2 < len(B):
            if A[p1] > B[p2]:
                res = min(res, A[p1] - B[p2])
                p2 += 1
            else:
                res = min(res, B[p2] - A[p1])
                p1 += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print (s.smallestDifference([3,4,6,7], [2,3,8,9]))
# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/7
# @Time: 15:04
# @url: http://www.lintcode.com/zh-cn/problem/median-of-two-sorted-arrays/
# @Description:两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        # 合并列表，然后排序
        newList = sorted(A + B)
        if not newList:
            return None
        # 偶数
        if len(newList) % 2 == 0:
            print newList[len(newList) / 2 - 1]
            return (newList[len(newList) / 2] + newList[len(newList) / 2 - 1]) / 2.0
            # 奇数
        else:
            return float(newList[int(len(newList) / 2)])
        return None


if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([], [1])

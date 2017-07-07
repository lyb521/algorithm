# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/7
# @Time: 14:04
# @url: http://www.lintcode.com/zh-cn/problem/single-number/
# @Description:给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """

    def singleNumber(self, A):
        # write your code here
        if len(A) == 0:
            return 0

        for i in A:
            if A.count(i) < 2:
                return i
        return 0

if __name__ == '__main__':
    s = Solution()
    print  s.singleNumber([1,2,2,1,3,4,3])
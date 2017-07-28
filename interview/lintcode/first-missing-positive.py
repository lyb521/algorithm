# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/28
# @Time: 16:33
# @url: http://www.lintcode.com/zh-cn/problem/first-missing-positive/
# @Description:给出一个无序的正数数组，找出其中没有出现的最小正整数。

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        A = sorted(filter(lambda t: t > 0, set(A)))
        print (A)
        if len(A) == 0:
            return 1
        if min(A) > 1:
            return 1
        for i in range(0, len(A)-1):
            if A[i] > 0 and A[i] + 1 != A[i+1]:
                return A[i] + 1
        if max(A) < 0:
            return 1
        else:
            return max(A)+1

if __name__ == '__main__':
    s = Solution()
    print (s.firstMissingPositive([2,2,4,0,1,3,3,3,4,3]))
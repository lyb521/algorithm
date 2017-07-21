# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/6
# @Time: 19:10
# @url: http://www.lintcode.com/zh-cn/problem/triangle-count/
# @Description: 三角形计数

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code hereedges = sorted(S, reverse=True)
        count = 0
        if not S or len(S) < 3:
            return count
        S.sort()
        for i in range(2, len(S)):
            longest = S[i]
            left = 0
            right = i - 1
            while left < right:
                if S[left] + S[right] <= longest:
                    left += 1
                elif S[left] + S[right] > longest:
                    count += right - left
                    right -= 1
        return count


if __name__ == '__main__':
    Solution = Solution()
    print (Solution.triangleCount([3,4,6,7]))

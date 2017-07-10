# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/10
# @Time: 15:11
# @url:http://www.lintcode.com/zh-cn/problem/climbing-stairs/
# @Description: 假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        record = [1, 1]
        if n >= 2:
            for i in range(2, n + 1):
                record.append(record[i - 1] + record[i - 2])
        return record[n]

if __name__ == '__main__':
    s = Solution()
    print  s.climbStairs(5)
# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/26
# @Time: 16:37
# @url: http://www.lintcode.com/zh-cn/problem/3sum/
# @Description:

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        result = []
        for n in range(0, len(numbers)-2):
            for m in range(n+1, len(numbers)-1):
                for p in range(m+1, len(numbers)):
                    if numbers[n]+numbers[m]+numbers[p] == 0:
                        res = [numbers[n], numbers[m], numbers[p]]
                        res.sort()
                        if res not in result:
                            result.append(res)
        return result

if __name__ == '__main__':
    s = Solution()
    print (s.threeSum([1,0,-1,-1,-1,-1,0,1,1,1]))
# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/10/10
# @Time: 15:16
# @url: http://www.lintcode.com/zh-cn/problem/hash-function/
# @Description:
#

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        sum = 0
        for char in key:
            sum = sum * 33 + ord(char)
            sum = sum % HASH_SIZE
        return sum

if __name__ == '__main__':
    s = Solution()
    print (s.hashCode("abcd", 1000))
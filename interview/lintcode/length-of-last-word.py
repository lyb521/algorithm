# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/28
# @Time: 17:24
# @url: http://www.lintcode.com/zh-cn/problem/binary-tree-maximum-node/
# @Description:给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。如果不存在最后一个单词，请返回 0

class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        if not s:
            return 0
        s_list = s.strip().split(' ')
        return len(s_list[-1])

if __name__ == '__main__':
    s = Solution()
    print (s.lengthOfLastWord("a"))